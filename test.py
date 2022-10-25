"""
  imessage_playlist.tests
  ~~~~~~~~~~~~~~~~~~~~~~~
"""

from .grouptext import (
  get_path_to_imessage_database,
  get_chat_identifier,
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

