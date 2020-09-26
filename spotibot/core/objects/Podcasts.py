
import json
import requests

from spotibot.core.objects import Time
from spotibot.core.objects.General import Image, ExternalId, ExternalUrl
from spotibot.mongo.utils.Handlers import object_handler, get_serializable


class Show:
    """Auto-generated attribute instantiation docstring for show
    object (simplified)

    Note: Parameter description in below docstring is populated based
    on the  descriptions at the following link:
    https://developer.spotify.com/documentation/web-
    api/reference/object-model

    Please consult their official documentation for more in-depth
    information & full-linking across pages.

    Attributes:
        available_markets (array of strings): A list of the countries in
            which the show can be played, identified by their ISO 3166-1
            alpha-2 code.
        copyrights (array of copyright objects): The copyright
            statements of the show.
        description (str): A description of the show.
        explicit (bool): Whether or not the show has explicit content
            (true = yes it does; false = no it does not OR unknown).
        external_urls (an external URL object): Known external URLs for
            this show.
        href (str): A link to the Web API endpoint providing full
            details of the show.
        id (str): The Spotify ID for the show.
        images (array of image objects): The cover art for the show in
            various sizes, widest first.
        is_externally_hosted (bool): True if all of the shows episodes
            are hosted outside of Spotifys CDN. This field might be
            ``null`` in some cases.
        languages (array of strings): A list of the languages used in
            the show, identified by their ISO 639 code.
        media_type (str): The media type of the show.
        name (str): The name of the show.
        publisher (str): The publisher of the show.
        type (str): The object type: show.
        uri (str): The Spotify URI for the show.
    """

    def __init__(self, show):
        if show:
            self.available_markets: str = \
                object_handler(show, 'available_markets')

            self.copyrights: str = \
                object_handler(show, 'copyrights')

            self.description: str = \
                object_handler(show, 'description')

            self.explicit: str = \
                object_handler(show, 'explicit')

            self.external_urls: ExternalUrl = \
                ExternalUrl(object_handler(show, 'external_urls'))

            self.href: str = \
                object_handler(show, 'href')

            self.id: str = \
                object_handler(show, 'id')

            self.images: list = \
                [Image(image) for image in show.get('images', [None])]

            self.is_externally_hosted: str = \
                object_handler(show, 'is_externally_hosted')

            self.languages: str = \
                object_handler(show, 'languages')

            self.media_type: str = \
                object_handler(show, 'media_type')

            self.name: str = \
                object_handler(show, 'name')

            self.publisher: str = \
                object_handler(show, 'publisher')

            self.type: str = \
                object_handler(show, 'type')

            self.uri: str = \
                object_handler(show, 'uri')

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


class Episode:
    """Auto-generated attribute instantiation docstring for episode
    object (full)

    Note: Parameter description in below docstring is populated based
    on the  descriptions at the following link:
    https://developer.spotify.com/documentation/web-
    api/reference/object-model

    Please consult their official documentation for more in-depth
    information & full-linking across pages.

    Attributes:
        audio_preview_url (str): A URL to a 30 second preview (MP3
            format) of the episode.  ``null`` if not available.
        description (str): A description of the episode.
        duration_ms (int): The episode length in milliseconds.
        explicit (bool): Whether or not the episode has explicit content
            (true = yes it does; false = no it does not OR unknown).
        external_urls (an external URL object): External URLs for this
            episode.
        href (str): A link to the Web API endpoint providing full
            details of the episode.
        id (str): The Spotify ID for the episode.
        images (array of image objects): The cover art for the episode
            in various sizes, widest first.
        is_externally_hosted (bool): True if the episode is hosted
            outside of Spotifys CDN.
        is_playable (bool): True if the episode is playable in the given
            market.  Otherwise false.
        language (str): Note: This field is deprecated and might be
            removed in the future.  Please use the ``languages`` field
            instead.  The language used in the episode, identified by a ISO
            639 code.
        languages (array of strings): A list of the languages used in
            the episode, identified by their ISO 639 code.
        name (str): The name of the episode.
        release_date (str): The date the episode was first released, for
            example ``"1981-12-15"``. Depending on the precision, it might
            be shown as ``"1981"`` or ``"1981-12"``.
        release_date_precision (str): The precision with which
            ``release_date`` value is known: ``"year"``, ``"month"``, or
            ``"day"``.
        resume_point (a resume point object): The users most recent
            position in the episode.  Set if the supplied access token is a
            user token and has the scope ``user-read-playback-position``.
        show (a simplified show object): The show on which the episode
            belongs.
        type (str): The object type: ``"episode"``.
        uri (str): The Spotify URI for the episode.
    """

    def __init__(self, episode):
        self.audio_preview_url: str = \
            object_handler(episode, 'audio_preview_url')

        self.description: str = \
            object_handler(episode, 'description')

        self.duration: Time.Timestamp = \
            Time.Timestamp(episode.get('duration_ms'), base='milliseconds')

        self.explicit: bool = \
            object_handler(episode, 'explicit')

        self.external_urls: ExternalUrl = \
            ExternalUrl(object_handler(episode, 'external_urls'))

        self.href: str = \
            object_handler(episode, 'href')

        self.id: str = \
            object_handler(episode, 'id')

        self.images: list = \
            object_handler(episode, 'images')

        self.is_externally_hosted: bool = \
            object_handler(episode, 'is_externally_hosted')

        self.is_playable: bool = \
            object_handler(episode, 'is_playable')

        self.language: str = \
            object_handler(episode, 'language')

        self.languages: list = \
            object_handler(episode, 'languages')

        self.name: str = \
            object_handler(episode, 'name')

        self.release_date: str = \
            object_handler(episode, 'release_date')

        self.release_date_precision: str = \
            object_handler(episode, 'release_date_precision')

        self.show: Show = \
            Show(episode.get('show'))

        self.type: str = \
            object_handler(episode, 'type')

        self.uri: str = \
            object_handler(episode, 'uri')

    def get_duration(self) -> Time.Timestamp:
        return self.duration

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

    def add_to_playlist(self, playlist_href: str, headers: dict):

        return requests.post(playlist_href,
                             data=json.dumps({'uris': [self.uri]}),
                             headers=headers)
