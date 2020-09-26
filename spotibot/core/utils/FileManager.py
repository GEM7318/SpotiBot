# Imports
import pandas as pd
import os
from spotibot.core.utils import Hasher as util


def get_activity_playlist_for_user():
    """
    Returns dictionary of user_id: user_activity_playlist_id from source csv.
    # Finds relative path for directory storing single user_playlist_bot.csv.
    # Extracts full path to first .csv file in directory (assumes only a
    # single file in the directory).
    # Imports df.
    # Uses utility function from utils.py to get a dictionary of {user_id:
    # playlist_id} where playlist_id is the user's 'My Listening History'
    # playlist.
    :return:
    """
    dir_user_activity_playlist = os.path.join(
        os.getcwd(), "_data", "UserDBO Playlists", "py_managed_user_playlist_dim"
    )

    path_to_file = [
        os.path.join(dir_user_activity_playlist, file)
        for file in os.listdir(dir_user_activity_playlist)
        if ".csv" in file
    ][0]

    df = pd.read_csv(path_to_file, na_values="nan")

    uid_pid_dict = util.dict_from_df(df, "user_id", "playlist_id")

    return uid_pid_dict


def get_user_dim_dict():
    """
    Returns dictionary of user_id: associated display name, href,
    and follower count.
    # Follows same logic as get_activity_playlist_for_user()
    """
    dir_user_activity_playlist = os.path.join(
        os.getcwd(), "_data", "UserDBO Information"
    )

    path_to_file = [
        os.path.join(dir_user_activity_playlist, file)
        for file in os.listdir(dir_user_activity_playlist)
        if ".csv" in file
    ][0]

    user_df = pd.read_csv(path_to_file)

    user_df.set_index("user_id", drop=True, inplace=True)

    user_dim_dict = user_df.to_dict("index")

    return user_dim_dict
