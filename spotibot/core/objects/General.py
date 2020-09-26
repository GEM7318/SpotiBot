import json
from spotibot.mongo.utils.Handlers import object_handler, get_serializable


class ExternalId:
    """Auto-generated attribute instantiation docstring for external
    ID object

    Note: Parameter description in below docstring is populated based
    on the  descriptions at the following link:
    https://developer.spotify.com/documentation/web-
    api/reference/object-model

    Please consult their official documentation for more in-depth
    information & full-linking across pages.

    Attributes:
        {key} (str): The identifier type, for example:- ``"isrc"`` -
            International Standard Recording Code- ``"ean"`` -
            International Article Number- ``"upc"`` - Universal Product
            Code
        {value} (str): An external identifier for the object.
    """

    def __init__(self, external_id: dict):

        self.typ: str = list(external_id.keys())[0]

        self.id: str = object_handler(external_id, self.typ)

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


class ExternalUrl:
    """Auto-generated attribute instantiation docstring for external
    URL object

    Note: Parameter description in below docstring is populated based
    on the  descriptions at the following link:
    https://developer.spotify.com/documentation/web-
    api/reference/object-model

    Please consult their official documentation for more in-depth
    information & full-linking across pages.

    Attributes:
        typ (str) The type of the URL, for example:- ``"spotify"`` -
            The Spotify URL for the object.
        url (str): An external, public URL to the object.
    """

    def __init__(self, url):

        self.typ: str = object_handler(url, "typ")

        self.url: str = object_handler(url, "url")

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


class Image:
    """Auto-generated attribute instantiation docstring for image
    object

    Note: Parameter description in below docstring is populated based
    on the  descriptions at the following link:
    https://developer.spotify.com/documentation/web-
    api/reference/object-model

    Please consult their official documentation for more in-depth
    information & full-linking across pages.

    Attributes:
        height (int): The image height in pixels.  If unknown: ``null``
            or not returned.
        url (str): The source URL of the image.
        width (int): The image width in pixels.  If unknown: ``null`` or
            not returned.
    """

    def __init__(self, image):
        if image:
            self.height: int = object_handler(image, "height")

            self.url: str = object_handler(image, "url")

            self.width: int = object_handler(image, "width")

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
