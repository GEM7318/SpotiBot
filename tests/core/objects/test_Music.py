
import os

from spotibot.core.objects import \
    Music

from spotibot.mongo.utils.Handlers import \
    is_jsonable


def test_instantiation_serialization(result: dict):
    """Tests the instantiation of SpotiBot objects from raw API responses
    and their conversion to byte-code based on the object's property's/methods

    Args:
        result: PyTest fixture containing a dictionary of object entries
        mirroring the below.

            {object name:
                (object Class,
                 raw API representation pre-instantiation,
                 representation post-instantiation as of last stable build
                 )
             }

        Objects currently covered are:
            : music.Track
            : music.Album
            : music.Artist
            : device.Device
            : context.Context
    """
    for obj_name, nested_val in result.items():
        spot_obj, result_in, expected_out = nested_val
        instantiated = spot_obj(result_in)
        assert instantiated == expected_out
        assert is_jsonable(instantiated.json)



# -----------------------------------------------------------------------------


# def test_album(result):
#     to_instantiate = result.get('item').get('album')
#     instantiated = Music.Album(to_instantiate)
#     assert isinstance(instantiated, Music.Album)
#
#
# def test_album_serialization(result):
#     to_instantiate = result.get('item').get('album')
#     instantiated = Music.Album(to_instantiate)
#     assert is_jsonable(instantiated.json)
