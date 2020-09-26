# import configparser
# import os

# config = configparser.ConfigParser()
# config.read(os.path.join(os.getcwd(), 'mongo_creds.cfg'))

from mongoengine import *

# from spotibot.mongo.conn import \
#     Connector as conn

# conn_str = conn.get_creds(collection='users')
# connect(host=conn_str)


class User(Document):
    username: str = StringField(required=True, primary_key=True)
    obj: str = StringField(required=True)

    meta = {"allow_inheritance": True, "collection": "users", "db": "SpotiBot"}
