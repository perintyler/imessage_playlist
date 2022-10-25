""""
  imessage_playlist.grouptext
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module is responsible for querying imessages from the local SQLite 
databse for a specific group text.
"""

import os
import pwd

def get_path_to_imessage_database() -> str:
  """
  For each OSX user, all imessages are stored in a local SQLite database stored at: "~/Library/Messages/chat.db".

  This function returns an absolute path for the currently logged-in OSX user.
  """
  osx_user_id = os.getuid()
  osx_user_account = pwd.getpwuid(osx_user_id)
  osx_username = osx_user_account.pw_name
  return os.path.join('/Users', osx_username, 'Library', 'Messages', 'chat.db')
