""""
  imessage_playlist.curate
  ~~~~~~~~~~~~~~~~~~~~~~~~

This module is responsible for creating a spotify playlist with a collection
of track links.
"""

import os
from argparse import ArgumentParser

from .grouptext import get_texts_for_group

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

def get_track_links_from_grouptext(group_name):
  """
  """
  spotify_links = []

  for text_message in get_texts_for_group(group_name):
    for word in text_message.split(' '):
      if word.startswith('https://open.spotify.com/track'):
        spotify_links.append(word)

  return spotify_links

def create_playlist_from_grouptext(playlist_name, group_name):
  """
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

if __name__ == '__main__':
  parser = ArgumentParser(description='Get all text messages for a iMessage group chat')
  parser.add_argument('--group', type=str)
  parser.add_argument('--playlist', type=str)
  args = parser.parse_args()

  print(create_playlist_from_grouptext(args.playlist, args.group))
