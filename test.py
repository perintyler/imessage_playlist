"""
  imessage_playlist.tests
  ~~~~~~~~~~~~~~~~~~~~~~~
"""

from .grouptext import (
  get_path_to_imessage_database,
  get_chat_identifier,
  get_texts_for_group,
)

from .curate import (
  get_track_links_from_grouptext,
)

import sqlite3

NAME_OF_TEST_IMESSAGE_GROUPCHAT = 'test group chat'

def test_get_path_to_imessage_database():
  assert get_path_to_imessage_database() \
      == '/Users/tylerperin/Library/Messages/chat.db'

def test_get_chat_identifier():
  connection = sqlite3.connect(get_path_to_imessage_database())
  assert get_chat_identifier(NAME_OF_TEST_IMESSAGE_GROUPCHAT, connection) \
     == 'chat131457465125669997'

def test_get_texts_for_group():
  assert get_texts_for_group(NAME_OF_TEST_IMESSAGE_GROUPCHAT) == [
    'https://youtu.be/EyeW_axUEQU',
    'Dummy message ',
    'https://open.spotify.com/track/3DbBgbnDUOml329rAp2Tbr?si=de627e1538c242e7',
    'froelich send a couple of Spotify links in here for me please ',
    'link in-between https://open.spotify.com/track/1x0WbCpdSPdwVoTCdJ4pPZ?si=7721bb5c607f4d7e a bunch of text',
    'https://open.spotify.com/track/5lw8Mgb4LyhriPIC86gV6e?si=cb9c17509a5e457a',
    'https://open.spotify.com/track/5lw8Mgb4LyhriPIC86gV6e?si=cb9c17509a5e457a',
    'duplicate link',
    'https://open.spotify.com/track/5xTtaWoae3wi06K5WfVUUH?si=gxXVvjBITqSvFIyu4mfR7A',
    'Laughed at “https://open.spotify.com/track/5xTtaWoae3wi06K5WfVUUH?si=gxXVvjBITqSvFIyu4mfR7A”',
    'Non Spotify link',
    'https://www.youtube.com/watch?v=fWTcct-uaH0&ab_channel=SoundWriter',
    'https://open.spotify.com/',
    'non-song Spotify link',
    'https://open.spotify.com/artist/6olE6TJLqED3rqDCT0FyPh?si=pnV4b9-VR5OLUZkLEP0l0Q',
    'non song link'
  ]

def test_get_track_links_from_grouptext():
  assert get_track_links_from_grouptext(NAME_OF_TEST_IMESSAGE_GROUPCHAT) == {
    'https://open.spotify.com/track/3DbBgbnDUOml329rAp2Tbr?si=de627e1538c242e7', 
    'https://open.spotify.com/track/1x0WbCpdSPdwVoTCdJ4pPZ?si=7721bb5c607f4d7e', 
    'https://open.spotify.com/track/5lw8Mgb4LyhriPIC86gV6e?si=cb9c17509a5e457a', 
    'https://open.spotify.com/track/5xTtaWoae3wi06K5WfVUUH?si=gxXVvjBITqSvFIyu4mfR7A'
  }
