
from mongoengine import *

from spotibot.mongo.conn import \
    Connector

from spotibot.mongo.objects import \
    General as genmongo


class Activity:

    def __init__(self, spot_obj):

        playback = \
            spot_obj.pop('playback')

        self.current = \
            genmongo.Current().from_json(spot_obj.json)

        current_typ = spot_obj.get('currently_playing_type')

        if current_typ == 'track':
            self.current.playback = genmongo.Track.from_json(playback.json)

        elif current_typ == 'episode':
            self.current.playback = genmongo.Episode.from_json(playback.json)

        else:
            self.current.playback = None

        # TODO: Switch this to be based off of currently_playing_type field
        #  instead of the object_map dictionary
        # embedded = \
        #     [v[0] for k, v in genmongo.object_map.items()
        #      if isinstance(playback, k)][0]
        #
        # self.current.playback = \
        #     embedded.from_json(playback.json)

    def save(self, **kwargs):
        return self.current.save(force_insert=True, **kwargs)
