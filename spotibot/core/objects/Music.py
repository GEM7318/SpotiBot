
import json
import requests

from spotibot.core.objects import \
    Time

from spotibot.core.objects.General import \
    Image, \
    ExternalUrl, \
    ExternalId

from spotibot.mongo.utils.Handlers import \
    object_handler, \
    get_serializable


class Album:
    """Auto-generated attribute instantiation docstring for album
    object (simplified)

    Note: Parameter description in below docstring is populated based
    on the  descriptions at the following link:
    https://developer.spotify.com/documentation/web-
    api/reference/object-model

    Please consult their official documentation for more in-depth
    information & full-linking across pages.

    Attributes:
        album_group (string, optional): The field is present when
            getting an artists albums.  Possible values are album, single,
            compilation, appears_on.  Compare to album_type this field
            represents relationship between the artist and the album.
        album_type (str): The type of the album: one of album, single,
            or compilation.
        artists (array of simplified artist objects): The artists of the
            album.  Each artist object includes a link in ``href`` to more
            detailed information about the artist.
        available_markets (array of strings): The markets in which the
            album is available: ISO 3166-1 alpha-2 country codes.  Note
            that an album is considered available in a market when at least
            1 of its tracks is available in that market.
        external_urls (an external URL object): Known external URLs for
            this album.
        href (str): A link to the Web API endpoint providing full
            details of the album.
        id (str): The Spotify ID for the album.
        images (array of image objects): The cover art for the album in
            various sizes, widest first.
        name (str): The name of the album.  In case of an album
            take-down, the value may be an empty string.
        release_date (str): The date the album was first released, for
            example ``1981``. Depending on the precision, it might be shown
            as ``1981-12`` or ``1981-12-15``.
        release_date_precision (str): The precision with which
            ``release_date`` value is known: ``year`` , ``month`` , or
            ``day``.
        restrictions (str): Part of the response when
            Track Relinking is applied, the original track is not available
            in the given market, and Spotify did not have any tracks to
            relink it with.  The track response will still contain metadata
            for the original track, and a restrictions object containing
            the reason why the track is not available: ``"restrictions" :
            {"reason" : "market"}``
        type (str): The object type: album
        uri (str): The Spotify URI for the album.
    """

    def __init__(self, album):

        self.album_type: str = \
            object_handler(album, 'album_type')

        self.artists: list = \
            [Artist(artist) for artist in object_handler(album, 'artists')]

        self.available_markets: list = \
            object_handler(album, 'available_markets')

        self.external_urls: ExternalUrl = \
            ExternalUrl(object_handler(album, 'external_urls'))

        self.href: str = \
            object_handler(album, 'href')

        self.id: str = \
            object_handler(album, 'id')

        self.images: list = \
            [Image(image) for image in object_handler(album, 'images')]

        self.name: str = \
            object_handler(album, 'name')

        self.release_date: str = \
            object_handler(album, 'release_date')

        self.release_date_precision: str = \
            object_handler(album, 'release_date_precision')

        self.restrictions: dict = \
            object_handler(album, 'restrictions')

        self.type: str = \
            object_handler(album, 'type')

        self.uri: str = \
            object_handler(album, 'uri')

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


class Artist:
    """Auto-generated attribute instantiation docstring for artist
    object (simplified)

    Note: Parameter description in below docstring is populated based
    on the  descriptions at the following link:
    https://developer.spotify.com/documentation/web-
    api/reference/object-model

    Please consult their official documentation for more in-depth
    information & full-linking across pages.

    Attributes:
        external_urls (an external URL object): Known external URLs for
            this artist.
        href (str): A link to the Web API endpoint providing full
            details of the artist.
        id (str): The Spotify ID for the artist.
        name (str): The name of the artist.
        type (str): The object type: ``"artist"``
        uri (str): The Spotify URI for the artist.
    """

    def __init__(self, artist):
        self.href: str = \
            object_handler(artist, 'href')

        self.id: str = \
            object_handler(artist, 'id')

        self.name: str = \
            object_handler(artist, 'name')

        self.type: str = \
            object_handler(artist, 'type')

        self.uri: str = \
            object_handler(artist, 'uri')

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


class Track:
    """Auto-generated attribute instantiation docstring for track
    object (full)

    Note: Parameter description in below docstring is populated based
    on the  descriptions at the following link:
    https://developer.spotify.com/documentation/web-
    api/reference/object-model

    Please consult their official documentation for more in-depth
    information & full-linking across pages.

    Attributes:
        album (a simplified album object): The album on which the track
            appears.  The album object includes a link in ``href`` to full
            information about the album.
        artists (an array of simplified artist objects): The artists who
            performed the track.  Each artist object includes a link in
            ``href`` to more detailed information about the artist.
        available_markets (array of strings): A list of the countries in
            which the track can be played, identified by their ISO 3166-1
            alpha-2 code.
        disc_number (int): The disc number (usually ``1`` unless the
            album consists of more than one disc).
        duration (int): The track length in milliseconds.
        explicit (Boolean): Whether or not the track has explicit lyrics
            ( ``true`` = yes it does; ``false`` = no it does not OR
            unknown).
        external_ids (an external ID object): Known external IDs for the
            track.
        external_urls (an external URL object): Known external URLs for
            this track.
        href (str): A link to the Web API endpoint providing full
            details of the track.
        id (str): The Spotify ID for the track.
        is_playable (bool): Part of the response when Track Relinking is
            applied.  If ``true`` , the track is playable in the given
            market.  Otherwise ``false``.
        linked_from (a linked track object): Part of the response when
            Track Relinking is applied, and the requested track has been
            replaced with different track.  The track in the
            ``linked_from`` object contains information about the
            originally requested track.
        restrictions (a restrictions object): Part of the response when
            Track Relinking is applied, the original track is not available
            in the given market, and Spotify did not have any tracks to
            relink it with.  The track response will still contain metadata
            for the original track, and a restrictions object containing
            the reason why the track is not available: ``"restrictions" :
            {"reason" : "market"}``
        name (str): The name of the track.
        popularity (int): The popularity of the track.  The value will
            be between 0 and 100, with 100 being the most popular.The
            popularity of a track is a value between 0 and 100, with 100
            being the most popular.  The popularity is calculated by
            algorithm and is based, in the most part, on the total number
            of plays the track has had and how recent those plays
            are.Generally speaking, songs that are being played a lot now
            will have a higher popularity than songs that were played a lot
            in the past.  Duplicate tracks (e.g.  the same track from a
            single and an album) are rated independently.  Artist and album
            popularity is derived mathematically from track popularity.
            Note that the popularity value may lag actual popularity by a
            few days: the value is not updated in real time.
        preview_url (str): A link to a 30 second preview (MP3 format) of
            the track.  Can be ``null``
        track_number (int): The number of the track.  If an album has
            several discs, the track number is the number on the specified
            disc.
        type (str): The object type: track.
        uri (str): The Spotify URI for the track.
        is_local (bool): Whether or not the track is from a local file.
    """

    def __init__(self, track: dict):

        self.album: Album = \
            Album(object_handler(track, 'album'))

        self.artists: list = \
            [Artist(artist) for artist in object_handler(track, 'artists')]

        self.available_markets: list = \
            object_handler(track, 'available_markets')

        self.disc_number: int = \
            object_handler(track, 'disc_number')

        self.duration: Time.Timestamp = \
            Time.Timestamp(track.get('duration_ms'), base='milliseconds')

        self.explicit: bool = \
            object_handler(track, 'explicit')

        self.external_ids: ExternalId = \
            ExternalId(object_handler(track, 'external_ids'))

        self.external_urls: ExternalUrl = \
            ExternalUrl(object_handler(track, 'external_urls'))

        self.href: str = \
            object_handler(track, 'href')

        self.id: str = \
            object_handler(track, 'id')

        self.is_local: bool = \
            object_handler(track, 'is_local')

        self.name: str = \
            object_handler(track, 'name')

        self.popularity: int = \
            object_handler(track, 'popularity')

        self.preview_url: str = \
            object_handler(track, 'preview_url')

        self.track_number: int = \
            object_handler(track, 'track_number')

        self.type: str = \
            object_handler(track, 'type')

        self.uri: str = \
            object_handler(track, 'uri')

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
