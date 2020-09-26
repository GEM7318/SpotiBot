import json
from spotibot.mongo.utils.Handlers import object_handler, get_serializable


class Context:
    """Auto-generated attribute instantiation docstring for context
    object

    Note: Parameter description in below docstring is populated based
    on the  descriptions at the following link:
    https://developer.spotify.com/documentation/web-
    api/reference/object-model

    Please consult their official documentation for more in-depth
    information & full-linking across pages.

    Attributes:
        type (str): The object type, e.g.  artist, playlist, album.
        href (str): A link to the Web API endpoint providing full
            details of the track.
        external_urls (an external URL object): External URLs for this
            context.
        uri (str): The Spotify URI for the context.
    """

    def __init__(self, context: dict):

        if context:
            self.href: str = object_handler(context, "href")

        if context:
            self.type: str = object_handler(context, "type")

        if context:
            self.uri: str = object_handler(context, "uri")

        if context:
            self.external_urls: str = object_handler(context, "external_urls")

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
