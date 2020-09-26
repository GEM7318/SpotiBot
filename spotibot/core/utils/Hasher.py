# Imports
import hashlib
import pandas as pd
import calendar
import datetime as dt


def quick_hash(unhashed):
    """
    Quick hashing function to truncate the length playlist_id:
    snapshot_id key.
    :param unhashed:
    :return:
    """
    hashed_base = hashlib.md5(unhashed.encode("utf-8"))
    hashed_str = hashed_base.hexdigest()
    return hashed_str


def dict_to_df(nested_dict, id_col="id"):
    """Fully flatten single-layer nested DataFrame into fully tabular form,
    distinct on
    'id' which is just a generated UUID for every time the script runs
    """
    df = pd.DataFrame(nested_dict.values(), index=nested_dict.keys())
    df.index.name = id_col
    df.reset_index(inplace=True)
    return df


def dict_from_df(df: pd.DataFrame, key_col: str, val_col: str) -> dict:
    """
    Simple helper function to return dictionary from two columns within a
    DataFrame
    :param df: DataFrame to extract dictionary from
    :param key_col: Column to serve as key in dictionary
    :param val_col: Column to serve as value in dictionary
    :return: Dictionary of distinct key: value pairs from column
    """
    to_return = {
        k: v[val_col]
        for k, v in df[[key_col, val_col]].set_index(key_col).to_dict("index").items()
        if str(v[val_col]) != "nan"
    }

    return to_return


def to_seconds(milliseconds):
    seconds = round(milliseconds / 1000, 2)
    return seconds


def abs_secs_delta_from_ms(ms1, ms2):
    seconds1 = round(ms1 / 1000, 2)
    seconds2 = round(ms2 / 1000, 2)
    abs_delta = round(abs(seconds1 - seconds2), 2)
    return abs_delta


def get_numeric_tmstmp(tmstmp, return_string=False):
    parsed_tmstmp = dp.parse(str(tmstmp))
    numeric_tmstmp = parsed_tmstmp.strftime("%Y%m%d%H%M%S%f")
    if return_string is True:
        return numeric_tmstmp
    else:
        return float(numeric_tmstmp)


#  -----------------
def iso8601_to_unix(iso_string, includes_tz=True):
    if includes_tz is True:
        return calendar.timegm(
            dt.datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S.%fZ").timetuple()
        )
    else:
        return calendar.timegm(
            dt.datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S.%f").timetuple()
        )


#  -----------------


def ns_to_seconds(epoch_ns):
    return epoch_ns * (1 / 1_000_000_000)


def ns_to_ms(epoch_ns):
    return epoch_ns * (1 / 1_000_000)


def ms_to_seconds(milliseconds):
    return milliseconds * (1 / 1_000)


def seconds_to_ms(seconds):
    return seconds * (1_000)
