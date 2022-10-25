"""
  imessage_playlist.setup
  ~~~~~~~~~~~~~~~~~~~~~~~

This file contains setup instructions for the `imessage_playlist` package
for easy installation.
"""

from setuptools import setup

PACKAGE_NAME = 'imessage_playlist'

setup(
  name=PACKAGE_NAME,
  package_dir={PACKAGE_NAME: '.'}, # source files are in the repos's root directory
)
