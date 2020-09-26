import configparser
import os


def get_creds(collection: str, database="SpotiBot"):

    config = configparser.ConfigParser()
    config.read(os.path.join(os.getcwd(), "mongo_creds.cfg"))

    conn_str = (
        f"mongodb+srv://{config.get('mongo', 'USERNAME')}:"
        f"{config.get('mongo', 'PASSWORD')}@"
        f"{config.get('mongo', 'DATABASE')}-gkkvg.mongodb"
        f".net/{config.get('mongo', 'COLLECTION')}?"
        f"retryWrites=true&w=majority"
    )
    # TODO: Figure out why feeding the collection name as arguments results
    #  in an invalid collection
    # conn_str = f"mongodb+srv://{config.get('mongo', 'USERNAME')}:" \
    #            f"{config.get('mongo', 'PASSWORD')}@" \
    #            f"{config.get('mongo', 'DATABASE')}-gkkvg.mongodb" \
    #            f".net/{collection}?" \
    #            f"retryWrites=true&w=majority"
    # conn_str = f"mongodb+srv://{config.get('mongo', 'USERNAME')}:" \
    #            f"{config.get('mongo', 'PASSWORD')}@" \
    #            f"SpotiBot-gkkvg.mongodb" \
    #            f".net/{collection}?" \
    #            f"retryWrites=true&w=majority"
    return conn_str
