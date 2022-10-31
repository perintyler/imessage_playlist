# iMessage Playlist

This python package can be used to create a spotify playlist containing all songs shared in an iMessage group text.

## Setup

### Installation

The `imessage_playlist` package and all of its dependencies can be installed with pip:

```bash
pip3 install .
```

### `chat.db` Permissions

An osx user's iMessage history is stored in a SQLite database called `chat.db`. In the `macOS Mojave` update, apple changed the default permissions for this `chat.db` file. In order to use `imessage_playlist`, you'll need to give `Terminal` full disk access. To do so:
1. navigate to `System Preferences`
2. select `Security & Privacy`
3. select the `Privacy` tab
4. In the scrollable section on the left, select `Full Disk Access`
5. In the scrollable section on the right, select the checkbox next to `Terminal`

Once this is done, `imessage_playlist` will be able query the local SQLite database.

