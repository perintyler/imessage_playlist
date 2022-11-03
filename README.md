# iMessage Playlist

This python package can be used to create a spotify playlist containing all songs shared in an iMessage group text.

```bash
% python3 -m imessage_playlist --group "My Group Chat" --playlist "My New Playlist"

Curated 16 songs from "My Group Chat" and saved them to new playlist "My New Playlist"
Link to playlist: https://open.spotify.com/playlist/2HyB1oMdu6iosGN3BXG8iS
```

## Setup

__Requirements:__
- python3
- OSX

### Installation

The `imessage_playlist` package and all of its dependencies can be installed with pip. Run this command from within the root repo directory:

```bash
pip3 install ./path/to/imessage_playlist
```

### Granting `chat.db` Permissions

An osx user's iMessage history is stored in a SQLite database called `chat.db`. In the `macOS Mojave` update, apple changed the default permissions for this `chat.db` file. In order to use `imessage_playlist`, you'll need to give `Terminal` full disk access. To do so:
1. navigate to `System Preferences`
2. select `Security & Privacy`
3. select the `Privacy` tab
4. In the scrollable section on the left, select `Full Disk Access`
5. In the scrollable section on the right, select the checkbox next to `Terminal`

Once this is done, `imessage_playlist` will be able query the local SQLite database.

### Providing Spotify Client Credentials

This package uses the Spotify API, which requires a client application. Unfortunately, in order to use `imessage_playlist`, you'll have to create your own client-application (since pushing my own client ID/secret would be a security risk). Once you've created your own spotify client application, create an `.env` file in the repo's root directory. Then, inside that file, define `SPOTIFY_CLIENT_ID`, `SPOTIFY_CLIENT_SECRET`, and `SPOTIFY_REDIRECT_URI`. 

The `SPOTIFY_REDIRECT_URI` will need to be whitelisted by your spotify client application. To do so:
1. navigate to the spotify developer dashboard
2. click on your applications
3. click the "edit settings" button
4. scroll down to the "Redirect URIs" section
5. enter your redirect URI in the prompt and select "add"

__NOTE:__ For local applications, use a redirect uri within the `localhost` domain, such as `http://localhost:8888/callback`.

For reference, use the `auth-template.env` enviroment file template, which is located in this repo's root directory.

## Testing

Tests were implemented using `pytest` and can be found in `tests.py`. I used my own local `chat.db` file for testing, and since I won't push my own iMessage database file to github, nobody else will be able to run the tests for now. If there's a need for it in the future, I can create a test `chat.db` with dummy data, which I would be able to push to github. 

