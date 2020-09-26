# ---------------/ Gets token object for a new user /--------------------------

import json
import jsonpickle
import time
from requests_oauth2 import OAuth2

from spotibot.mongo.utils.Handlers import get_serializable

from spotibot.core.objects import Time as spottime

from spotibot.mongo.core.objects import User as UserDoc


# from spotibot.mongo.conn import \
#     Connector


class SpotifyClient(OAuth2):
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


class Client:
    def __init__(self, cfg: dict):
        self.cfg = cfg

        attrs = cfg.get("CLIENT")

        self.client_id = attrs.get("CLIENT_ID")

        self.client_secret = attrs.get("CLIENT_SECRET")

        self.redirect_uri = attrs.get("REDIRECT_URI")


class API(Client):
    def __init__(self, cfg: dict):
        super().__init__(cfg)

        attrs = self.cfg.get("AUTH")

        self.site = attrs.get("SITE")

        self.authorization_url = attrs.get("AUTHORIZATION_URL")

        self.token_url = attrs.get("TOKEN_URL")

        self.scope = attrs.get("SCOPE")


class Auth(API):
    def __init__(self, cfg: dict, username: str):
        super().__init__(cfg)

        self.username = username

        self.creds = SpotifyClient(
            site=self.site,
            authorization_url=str(self.authorization_url),
            token_url=self.token_url,
            scope_sep=" ",
            client_id=self.client_id,
            client_secret=self.client_secret,
            redirect_uri=self.redirect_uri,
        )

        self.authorized_url = self.creds.authorize_url(
            scope=self.scope, response_type="code", username=username
        )

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


class Token:
    def __init__(self, authorized: Auth, url: str):

        self.authorized = authorized

        _, self.code = url.split(r"?code=")

        self.grant_time = int(time.time())

        self.data = self.authorized.creds.get_token(
            code=self.code,
            grant_type="authorization_code",
            redirect_uri=self.authorized.redirect_uri,
        )

        self.retries: list = []

    @property
    def access_token(self):
        return self.data.get("access_token")

    @property
    def refresh_token(self):
        return self.data.get("refresh_token")

    @property
    def expiration_time(self):
        return self.grant_time + self.data.get("expires_in")

    @property
    def scope(self):
        return self.scope

    @property
    def is_expired(self):
        try:
            return (self.expiration_time - 10) < time.time()
        except IOError as e:
            print(e)

    @property
    def expires_in(self):
        return spottime.Timestamp(
            (self.expiration_time - 10) - time.time(), base="seconds"
        )

    def refresh(self):

        self.grant_time = int(time.time())

        data_refresh = self.authorized.creds.refresh_token(
            grant_type="refresh_token", refresh_token=self.refresh_token,
        )

        if not data_refresh.get("access_token"):

            data_refresh = self.authorized.creds.refresh_token(
                grant_type="refresh_token", refresh_token=self.refresh_token,
            )

            self.retries.append(vars(data_refresh))

        assert data_refresh.get(
            "access_token"
        ), f"Access token not returned after {len(self.retries)} retries"

        self.data.update(data_refresh)

        return self

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


class UserDBI:
    def __init__(self, token: Token):
        self.token = token

        self.username = self.token.authorized.username

        self.pickled = jsonpickle.encode(self.token)

        self.mongo = UserDoc.User.from_json(
            json.dumps({"username": self.username, "obj": self.pickled})
        )

    def save(self, **kwargs):
        if UserDoc.User.objects(pk=self.username).first():
            UserDoc.User.objects(pk=self.username).delete()
            self.mongo.save(force_insert=True, **kwargs)

        return self

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
