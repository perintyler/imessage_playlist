""""
  imessage_playlist.curate
  ~~~~~~~~~~~~~~~~~~~~~~~~

This module is responsible for creating a spotify playlist with a collection
of track links.
"""

def get_track_links_from_grouptext(group_name):
  """
  """
  spotify_links = []

  for text_message in get_texts_for_group(group_name):
    for word in text_message.split(' '):
      if word.startswith('https://open.spotify.com/track'):
        spotify_links.append(word)

  return spotify_links
