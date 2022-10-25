""""
  imessage_playlist.grouptext
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module is responsible for querying imessages from the local SQLite 
databse for a specific group text.
"""

import os
import pwd

import pandas as pd

def get_path_to_imessage_database() -> str:
  """
  For each OSX user, all imessages are stored in a local SQLite database stored at: "~/Library/Messages/chat.db".

  This function returns an absolute path for the currently logged-in OSX user.
  """
  osx_user_id = os.getuid()
  osx_user_account = pwd.getpwuid(osx_user_id)
  osx_username = osx_user_account.pw_name
  return os.path.join('/Users', osx_username, 'Library', 'Messages', 'chat.db')

def get_chat_identifier(group_name: str, connection: sqlite3.Connection) -> str:
  """
  Every group text has a unique identifier, since multiple group texts can have the same
  display name. It will look something like this: 'chat131457465125669997'

  - group_name: the display name shown at the top when a group text is selected
  - connection: an open connection to the imessage SQLite database
  """
  chat_query = pd.read_sql_query(f"SELECT chat_identifier FROM chat WHERE display_name = '{group_name}'", connection)

  if len(chat_query) == 0:
    raise ValueError(f'No group texts exists for group name {group_name}')
  if len(chat_query) > 1:
    raise ValueError(f'There is more than one group for group name {group_name}')

  return chat_query['chat_identifier'][0]
