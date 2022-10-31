"""
  imessage_playlist.setup
  ~~~~~~~~~~~~~~~~~~~~~~~

This file contains setup instructions for the `imessage_playlist` package
for easy installation.
"""

from setuptools import setup

PACKAGE_NAME = 'imessage_playlist'

with open('./requirements.txt') as f:
  requirements = f.read().splitlines()

setup(
  name=PACKAGE_NAME,
  package_dir={PACKAGE_NAME: '.'}, # source files are in the repos's root directory
  install_requires=requirements # requirements outlined in `requirements.txt`
)
