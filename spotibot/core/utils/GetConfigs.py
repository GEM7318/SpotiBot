
# Imports
import configparser
import os


def get_spotify_creds():
    """
    Function to read in Spotify API credentials from configuration file.
    :return: Tuple of client ID, client secret, and username
    """
    config = configparser.ConfigParser()
    config.read(os.path.join(os.getcwd(), 'SpotiBot.ini'))

    client_id = config.get('CLIENT', 'CLIENT_ID')
    client_secret = config.get('CLIENT', 'CLIENT_SECRET')
    username_str = str(config.get('USER', 'USERNAME'))

    return client_id, client_secret, username_str
