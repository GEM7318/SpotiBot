import json
import jsonpickle
import requests
from mongoengine import *

from spotibot.mongo.utils.Handlers import get_serializable

from spotibot.mongo.core.objects import User as UserDoc

from spotibot.base.auth import OAuth as oauth

from spotibot.core.endpoints import Generic as genhref

from spotibot.base.config import Configuration

from spotibot.mongo.conn import Connector

from spotibot.core.objects import Music as music, Podcasts as podcasts

connect(host=Connector.get_creds(collection="users"))

config = Configuration.Config()

activity_playlists = config.get_configs(["PLAYLISTS", "ACTIVITY"])

activity_names_to_desc = {
    activity_playlists.get("MUSIC")
    .get("NAME"): activity_playlists.get("MUSIC")
    .get("DESCRIPTION"),
    activity_playlists.get("PODCASTS")
    .get("NAME"): activity_playlists.get("PODCASTS")
    .get("DESCRIPTION"),
}


def get_user_playlists(href, headers):
    request = requests.get(href, headers=headers)
    result = request.json()

    all_playlists = [result["items"]]
    while result.get("next"):
        result = requests.get(result.get("next"), headers=headers).json()
        all_playlists.append(result["items"])

    all_playlists = {
        t.get("name"): t.get("href") for batch in all_playlists for t in batch
    }

    return all_playlists


class UserDBO(genhref.Href):
    def __init__(self, user_id: str):

        super().__init__(username=user_id)

        self.user_id: str = user_id

        self.mongo_user = UserDoc.User.objects(pk=user_id).first()

        self.tokens: oauth.Token = jsonpickle.decode(self.mongo_user.obj)

        # Checking for activity playlists and creating if not pre-existing
        activity_names_to_types = {
            config.get_configs(["PLAYLISTS", "ACTIVITY", "MUSIC", "NAME"]): music.Track,
            config.get_configs(
                ["PLAYLISTS", "ACTIVITY", "PODCASTS", "NAME"]
            ): podcasts.Episode,
        }

        names_to_hrefs = {
            k: v
            for k, v in get_user_playlists(self.playlists, self.headers()).items()
            if activity_names_to_types.get(k)
        }

        activity_names_to_create = [
            k for k in activity_names_to_types.keys() if not names_to_hrefs.get(k)
        ]

        for name in activity_names_to_create:
            desc = activity_names_to_desc.get(name)
            req_href, req_payload = self.new_playlist(
                playlist_name=name, playlist_desc=desc
            )

            request = requests.post(req_href, data=req_payload, headers=self.headers())
            if request.ok:
                result = request.json()
                names_to_hrefs.update({result.get("name"): result.get("href")})

        activity_playlist_hrefs = {
            "track": names_to_hrefs.get(activity_playlists.get("MUSIC").get("NAME")),
            "episode": names_to_hrefs.get(
                activity_playlists.get("PODCASTS").get("NAME")
            ),
        }

        self.activity_playlist_hrefs = {
            k: f"{v}/tracks?" for k, v in activity_playlist_hrefs.items()
        }

    def refresh_tokens(self):
        self.tokens = self.tokens.refresh()
        self.mongo_user = oauth.UserDBI(self.tokens).save()

        return self

    def headers(self, post=False):

        if self.tokens.is_expired:
            self.refresh_tokens()

        if not post:
            return {"Authorization": f"Bearer {self.tokens.access_token}"}
        else:
            return {
                "Authorization": f"Bearer {self.tokens.access_token}",
                "Content-Type": "application/json",
            }

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


# test = UserDBO('125393293')
# test.tokens.is_expired
