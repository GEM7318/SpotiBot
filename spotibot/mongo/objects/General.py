import configparser
import os

config = configparser.ConfigParser()

config.read(os.path.join(os.getcwd(), 'mongo_creds.cfg'))

from mongoengine import *

from spotibot.core.objects import \
    Activity as act, \
    Music as music, \
    Podcasts as podcasts, \
    Device as device, \
    Time as spottime, \
    General as gen, \
    Context as cont


class Timestamp(EmbeddedDocument):
    raw: int = \
        IntField(required=False)

    base: str = \
        StringField(required=False)

    adj_ms: int = \
        IntField(required=False)

    adj_ns: int = \
        IntField(required=False)

    adj_sec: int = \
        IntField(required=False)

    seconds: int = \
        IntField(required=False)

    milliseconds: int = \
        IntField(required=False)

    nanoseconds: int = \
        IntField(required=False)

    minutes: int = \
        IntField(required=False)

    is_positive: bool = \
        BooleanField(required=False)

    is_negative: bool = \
        BooleanField(required=False)

    is_zero: bool = \
        BooleanField(required=False)

    meta = \
        {'allow_inheritance': True,
         'collection': 'activity',
         'db': 'SpotiBot'}


class Device(EmbeddedDocument):
    is_active: bool = \
        BooleanField(required=False)

    is_private_session: bool = \
        BooleanField(required=False)

    is_restricted: bool = \
        BooleanField(required=False)

    name: str = \
        StringField(required=False)

    type: str = \
        StringField(required=False)

    volume_percent: int = \
        IntField(required=False)

    meta = \
        {'allow_inheritance': True,
         'collection': 'activity',
         'db': 'SpotiBot'}


class ExternalId(EmbeddedDocument):
    typ: str = \
        StringField(required=False)

    id: str = \
        StringField(required=False)

    meta = \
        {'allow_inheritance': True,
         'collection': 'activity',
         'db': 'SpotiBot'}


class ExternalUrl(EmbeddedDocument):
    typ: str = \
        StringField(required=False)

    url: str = \
        StringField(required=False)

    spotify: str = \
        StringField(required=False)

    meta = \
        {'allow_inheritance': True,
         'collection': 'activity',
         'db': 'SpotiBot'}


class Image(EmbeddedDocument):
    url: str = \
        StringField(required=False, primary_key=True)

    height: int = \
        IntField(required=False)

    width: int = \
        IntField(required=False)

    id: str = \
        StringField(required=False, primary_key=False)

    meta = \
        {'allow_inheritance': True,
         'collection': 'activity',
         'db': 'SpotiBot'}


class Artist(EmbeddedDocument):
    external_urls = \
        EmbeddedDocumentField(ExternalUrl, required=False)

    external_ids = \
        EmbeddedDocumentField(ExternalId, required=False)

    followers: dict = \
        DictField(required=False)

    genres = \
        ListField(required=False)

    href: str = \
        StringField(required=False)

    id: str = \
        StringField(required=False, primary_key=True)

    images = \
        ListField(required=False)

    name: str = \
        StringField(required=False)

    popularity: int = \
        IntField(required=False)

    type: str = \
        StringField(required=False)

    uri: str = \
        StringField(required=False)

    meta = \
        {'allow_inheritance': True,
         'collection': 'activity',
         'db': 'SpotiBot'}


class Album(EmbeddedDocument):
    # _id: str = StringField(required=True, primary_key=True)

    album_type: str = \
        StringField(required=False)

    artists: list = \
        ListField(EmbeddedDocumentField(Artist, required=False))

    available_markets: list = \
        ListField(required=False)

    external_urls = \
        EmbeddedDocumentField(ExternalUrl, required=False)

    href: str = \
        StringField(required=False)

    id: str = \
        StringField(required=False, primary_key=True)

    images: list = \
        ListField(EmbeddedDocumentField(Image, required=False))

    name: str = \
        StringField(required=False)

    release_date: str = \
        StringField(required=False)

    release_date_precision: str = \
        StringField(required=False)

    restrictions: str = \
        StringField(required=False)

    type: str = \
        StringField(required=False)

    uri: str = \
        StringField(required=False)

    meta = \
        {'allow_inheritance': True,
         'collection': 'activity',
         'db': 'SpotiBot'}


class Track(EmbeddedDocument):
    # _id: str = StringField(required=True, primary_key=True)

    album = \
        EmbeddedDocumentField(Album, required=False)

    artists: list = \
        ListField(EmbeddedDocumentField(Artist, required=False))

    available_markets = \
        ListField(required=False)

    disc_number: int = \
        IntField(required=False)

    duration: int = \
        EmbeddedDocumentField(Timestamp, required=False)

    explicit = \
        BooleanField(required=False)

    external_ids = \
        EmbeddedDocumentField(ExternalId, required=False)

    external_urls = \
        EmbeddedDocumentField(ExternalUrl, required=False)

    href: str = \
        StringField(required=False)

    id: str = \
        StringField(required=False, primary_key=True)

    is_playable: bool = \
        BooleanField(required=False)

    linked_from = \
        StringField(required=False)

    restrictions = \
        StringField(required=False)

    name: str = \
        StringField(required=False)

    popularity: int = \
        IntField(required=False)

    preview_url: str = \
        StringField(required=False)

    track_number: int = \
        IntField(required=False)

    type: str = \
        StringField(required=False)

    uri: str = \
        StringField(required=False)

    is_local: bool = \
        BooleanField(required=False)

    meta = \
        {'allow_inheritance': True,
         'collection': 'activity',
         'db': 'SpotiBot'}


class Show(EmbeddedDocument):
    # _id: str = StringField(required=True, primary_key=True)

    available_markets = \
        ListField(required=False)

    copyrights: str = \
        StringField(required=False)

    description: str = \
        StringField(required=False)

    explicit: bool = \
        BooleanField(required=False)

    external_urls = \
        EmbeddedDocumentField(ExternalUrl, required=False)

    href: str = \
        StringField(required=False)

    id: str = \
        StringField(required=False)

    images: list = \
        ListField(EmbeddedDocumentField(Image, required=False))

    is_externally_hosted: bool = \
        BooleanField(required=False)

    language: str = \
        StringField(required=False)

    media_type: str = \
        StringField(required=False)

    name: str = \
        StringField(required=False)

    publisher: str = \
        StringField(required=False)

    type: str = \
        StringField(required=False)

    uri: str = \
        StringField(required=False)

    meta = \
        {'allow_inheritance': True,
         'collection': 'activity',
         'db': 'SpotiBot'}


class Episode(EmbeddedDocument):
    audio_preview_url: str = \
        StringField(required=False)

    description: str = \
        StringField(required=False)

    duration: int = \
        EmbeddedDocumentField(Timestamp, required=False)

    explicit: bool = \
        BooleanField(required=False)

    external_urls = \
        EmbeddedDocumentField(ExternalUrl, required=False)

    href: str = \
        StringField(required=False)

    id: str = \
        StringField(required=False)

    images: list = \
        ListField(EmbeddedDocumentField(Image, required=False))

    is_externally_hosted: bool = \
        BooleanField(required=False)

    is_playable: bool = \
        BooleanField(required=False)

    language: str = \
        StringField(required=False)

    languages = \
        ListField(required=False)

    name: str = \
        StringField(required=False)

    release_date: str = \
        StringField(required=False)

    release_date_precision: str = \
        StringField(required=False)

    resume_point = \
        StringField(required=False)

    show = \
        StringField(required=False)

    type: str = \
        StringField(required=False)

    uri: str = \
        StringField(required=False)

    meta = \
        {'allow_inheritance': True,
         'collection': 'activity',
         'db': 'SpotiBot'}


class Response(EmbeddedDocument):
    # _id: str = StringField(required=False, primary_key=True)

    ok: bool = \
        BooleanField(required=False)

    status_code: int = \
        IntField(required=False)

    result: dict = \
        DictField(required=False)

    meta = \
        {'allow_inheritance': True,
         'collection': 'activity',
         'db': 'SpotiBot'}


class Request(DynamicEmbeddedDocument):
    user_id: str = StringField(required=False)

    activity_endpoint: str = StringField(required=False)

    user_activity_playlist_id: str = StringField(required=False)

    unix_request_tmstmp: Timestamp = \
        EmbeddedDocumentField(Timestamp, required=False)

    # response: Response = \
    #     EmbeddedDocumentField(Response, required=False)

    endpoint_id: str = \
        StringField(required=False, primary_key=True)

    ok: bool = \
        BooleanField(required=False)

    meta = \
        {'allow_inheritance': True,
         'collection': 'activity',
         'db': 'SpotiBot'}


class Context(EmbeddedDocument):
    href: str = \
        StringField(required=False)

    type: str = \
        StringField(required=False)

    uri: str = \
        StringField(required=False)

    external_urls = \
        EmbeddedDocumentField(ExternalUrl, required=False)

    meta = \
        {'allow_inheritance': True,
         'collection': 'activity',
         'db': 'SpotiBot'}


class Current(DynamicDocument):
    # TODO: In rest of script, change the built-in `.save()` method to use
    #  the `.save()` method automatically inherited from Document and
    #  DynamicDocument via the following source:
    #  https://realpython.com/introduction-to-mongodb-and-python/

    _id: str = \
        StringField(required=False, primary_key=True)

    user_id: str = \
        StringField(required=False)

    activity_endpoint: str = \
        StringField(required=False)

    user_playlist_dict: dict = \
        DictField(required=False)

    user_activity_playlist_id: str = \
        StringField(required=False)

    unix_request_tmstmp: Timestamp = \
        EmbeddedDocumentField(Timestamp, required=False)

    # response: Response = \
    #     EmbeddedDocumentField(Response, required=False)

    endpoint_id: str = \
        StringField(required=False)

    ok: bool = \
        BooleanField(required=False)

    # request: Request = \
    #     EmbeddedDocumentField(Request, required=False)

    playback = \
        GenericEmbeddedDocumentField(required=True)

    context: Context = \
        EmbeddedDocumentField(Context, required=False)

    device: list = \
        ListField(EmbeddedDocumentField(Device, required=False))

    currently_playing_type: str = \
        StringField(required=False)

    shuffle_state: bool = \
        BooleanField(required=False)

    repeat_state: str = \
        StringField(required=False)

    actions: dict = \
        DictField(required=False)

    is_playing: bool = \
        BooleanField(required=False)

    progress: Timestamp = \
        EmbeddedDocumentField(Timestamp, required=False)

    # unix_request_tmstmp: Timestamp = \
    #     EmbeddedDocumentField(Timestamp, required=False)

    unix_refresh_tmstmp: Timestamp = \
        EmbeddedDocumentField(Timestamp, required=False)

    time_remaining: Timestamp = \
        EmbeddedDocumentField(Timestamp, required=False)

    unix_start_tmstmp: Timestamp = \
        EmbeddedDocumentField(Timestamp, required=False)

    unix_expected_end_tmstmp: Timestamp = \
        EmbeddedDocumentField(Timestamp, required=False)

    time_listened: Timestamp = \
        EmbeddedDocumentField(Timestamp, required=False)

    activity_id: str = \
        StringField(required=False)

    meta = \
        {'allow_inheritance': True,
         'collection': 'activity',
         'db': 'SpotiBot'}


object_map = {
    music.Album: (Album(), Album),
    music.Track: (Track(), Track),
    music.Artist: (Artist(), Artist),
    gen.ExternalUrl: (ExternalUrl(), ExternalUrl),
    spottime.Timestamp: (Timestamp(), Timestamp),
    gen.Image: (Image(), Image),
    cont.Context: (Context(), Context),
    device.Device: (Device(), Device),
    podcasts.Episode: (Episode(), Episode),
    podcasts.Show: (Show(), Show)}
    # act.Request: (Request(), Request)}
from spotibot.core.objects import Activity as activity