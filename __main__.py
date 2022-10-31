"""
  imessage_playlist Main Module
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Entry point for the `imessage_playlist` package
"""

from argparse import ArgumentParser
from dotenv import load_dotenv

from .curate import create_playlist_from_grouptext

# load Spotify API Credentials
load_dotenv()

# parse user input
parser = ArgumentParser(description='Get all text messages for a iMessage group chat')
parser.add_argument('--group', type=str)
parser.add_argument('--playlist', type=str)
args = parser.parse_args()

# query imessages and create playlist
playlist = create_playlist_from_grouptext(args.playlist, args.group)

# print success message
num_tracks = len(playlist['tracks']['items'])
playlist_link = playlist['external_urls']['spotify']
print(f'Curated {num_tracks} songs from "{args.group}" and saved them to new playlist "{args.playlist}"')
print(f'Link to playlist: {playlist_link}')

