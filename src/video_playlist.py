"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""
    def __init__(self):
        #playlist constructor
    self._playlist = {}

    def get_all_playlist(self):
        #returns all available playlist
        return list(self._playlist.values())

    def get_playlist(self, playlist_name):
        #returns playlists as objects.
        return self._playlist.get(playlist_name, None)