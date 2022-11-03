""""
  imessage_playlist.curate
  ~~~~~~~~~~~~~~~~~~~~~~~~

This module is responsible for creating a spotify playlist with a collection
of track links.
"""

import os
from typing import Set, Dict
from argparse import ArgumentParser

from .grouptext import get_texts_for_group

import spotipy
from spotipy.oauth2 import SpotifyOAuth

# https://developer.spotify.com/documentation/web-api/reference/#/operations/add-tracks-to-playlist
# The spotify API lets you add up to 100 songs to a playlist at a time 
SPOTIFY_SONG_ADDING_THRESHOLD = 100 

def get_track_links_from_grouptext(group_name: str) -> Set[str]:
  """
  Finds and returns all spotify track links that appear anywhere 
  in any text message found in a group chat.

  - group_name: the display name of an iMessage group
  """
  spotify_links = set()

  for text_message in get_texts_for_group(group_name):
    for word in text_message.split(' '):
      if word.startswith('https://open.spotify.com/track'):
        spotify_links.add(word)

  return spotify_links

def create_playlist_from_grouptext(playlist_name: str, group_name: str) -> Dict:
  """
  Creates a new spotify playlist, which will contain all songs shared in
  an iMessage group. This function will trigger a spotify authorization 
  workflow, allowing the user to log in to their spotify account in their 
  browser.

  - playlist_name: the name of the playlist to be created
  - group_name: the display name of an iMessage group

  Returns a dictionary representation of a spotify playlist object, which will 
  contain serialized JSON data describing the created playlist (refer to the 
  Spotify API Docs for details).
  """
  track_links = get_track_links_from_grouptext(group_name)

  spotify_client = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope='playlist-modify-private', 
    client_id=os.getenv('SPOTIFY_CLIENT_ID'),
    client_secret=os.getenv('SPOTIFY_CLIENT_SECRET'),
    redirect_uri=os.getenv('SPOTIFY_REDIRECT_URI')
  ))

  user_id = spotify_client.current_user()['id']
  playlist = spotify_client.user_playlist_create(user_id, playlist_name, public=False, collaborative=False)
  spotify_client.playlist_add_items(playlist['id'], items=track_links)

  return spotify_client.playlist(playlist['id'])

if __name__ == '__main__':
  parser = ArgumentParser(description='Get links to every spotify track shared in an iMessage group chat')
  parser.add_argument('group', type=str)
  args = parser.parse_args()
  for link in get_track_links_from_grouptext(args.group):
    print(link)
