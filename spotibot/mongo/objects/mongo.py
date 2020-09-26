import configparser
import os
import pickle
import jsonpickle

from spotibot.mongo.conn import Connector

from spotibot.mongo.objects import General as genmong

from mongoengine import *

pkl_dir = os.path.join(os.getcwd(), "_pkl")

connect(host=Connector.get_creds(collection="activity"))

with open(os.path.join(pkl_dir, "activity2.pkl"), "rb") as r:
    activity2 = pickle.load(r)


track_in = activity2.cached[3].playback

mongo_track = genmong.Track()
mongo_track["obj"] = jsonpickle.encode(track_in)
mongo_track["_id"] = track_in.id

mongo_track.save(force_insert=True)

mongo_track_out = genmong.Track.objects(pk=track_in.id).first()

mongo_track_out_dec = jsonpickle.decode(mongo_track_out["obj"])

type(track_in)
type(mongo_track)
type(mongo_track_out)
type(mongo_track_out_dec)
