import json
import requests

from spotibot.mongo.utils.Handlers import get_serializable

from spotibot.base.config import Configuration

config = Configuration.Config()

# class Request:
#
#     def __init__(self, href: str, headers: dict):


class Playlist:
    def __init__(self, href: str, headers: dict):

        self.href = href

        self.headers = headers

        request = requests.get(href, headers=headers)

        if request.ok:
            self.result = request.json()


class Href:
    def __init__(self, username: str):
        self.username = username

        self.current_playback = (
            r"https://api.spotify.com/v1/me/player?" r"additional_types=track,episode"
        )

    @property
    def playlists(self):
        return (
            f"https://api.spotify.com/v1/users/" f"{self.username}/playlists?limit=50"
        )

    @property
    def tracks_all_time(self):
        return

    def new_playlist(self, playlist_name: str, playlist_desc: str = None):
        href = f"https://api.spotify.com/v1/users/{self.username}/playlists"
        payload = json.dumps({"name": playlist_name, "description": playlist_desc})

        return href, payload

    def __eq__(self, other) -> bool:
        """Equality comparison to other objects.

        Args:
            other: Comparison object

        Returns:
            Boolean value indicating whether or not the attributes and their
            associated values are equal between the two objects
        """
        return vars(self) == vars(other)

    def __getitem__(self, item: str):
        """Getter method for subscriptability.

        Args:
            item: Attribute to get the value of

        Returns:
            Attribute value if exists in object's namespace
        """
        return getattr(self, item)

    def get(self, item: str, default=None):
        """Method for extracting attributes without throwing existence errors.

        Args:
            item: Attribute to get the value of
            default: Return value if attribute doesn't exist

        Returns:
            Attribute value or default if attribute does not exist
        """
        return vars(self).get(item, default)

    def to_dict(self) -> dict:
        """Calling utility serialization method on all attributes.

        Returns:
            String following valid json structure for mongo serialization.
        """
        return {k: get_serializable(v) for k, v in vars(self).items()}

    @property
    def json(self) -> str:
        """Jsonified/string attribute for all SpotiBot objects for mongo
        serialization purposes

        Returns:
            Serializable 'json' output of SpotiBot object
        """
        return json.dumps(self.to_dict())
