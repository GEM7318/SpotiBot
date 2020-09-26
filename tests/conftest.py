

import pytest
import os
import pickle
import json

from spotibot.core.objects import \
    Music as music, \
    Podcasts as podcast, \
    Context as context, \
    Device as device

fixture_src_dir = os.path.join(os.getcwd(), '_pytest_Fixture_src')

pickle_obj_map: dict = \
    {'track~full': music.Track,
     'album~simplified': music.Album,
     'artist~simplified': music.Artist,
     'device~base': device.Device,
     'context~base': context.Context
     }


@pytest.fixture(
    params=[
        (pickle_obj_map, fixture_src_dir)],

    scope='module'
)
def result(request):

    fixture = {}

    obj_map, src_dir = request.param

    for obj_name, spot_obj in obj_map.items():

        in_dir = os.path.join(src_dir, f"in_{obj_name}.pkl")
        out_dir = os.path.join(src_dir, f"out_{obj_name}.pkl")

        with open(in_dir, 'rb') as r:
            result_in = pickle.load(r)

        with open(out_dir, 'rb') as r2:
            expected_out = pickle.load(r2)

        fixture[obj_name] = (spot_obj, result_in, expected_out)

    return fixture


# TODO: Add other objects and clean up the code/re-factor if needed
# -----------------------------------------------------------------------------


# @pytest.fixture(
#     params=[
#         r'activity_result_track.pkl'],
#     #     ({'attr': 2}, 'attr', 2)
#     # ],
#     scope='module'
# )
# def result(request):
#     dir_to_open = os.path.join(fixture_src_dir, request.param)
#
#     with open(dir_to_open, 'rb') as r:
#         result = pickle.load(r)
#
#     return result

