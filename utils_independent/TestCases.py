from spotibot.core.objects import User as user
import requests

import pickle
import os

from spotibot.core.objects import \
    Music as music, \
    Podcasts as podcast, \
    Context as context, \
    Device as device


gem = user.UserDBO('125393293')

request = requests.get(gem.current_playback, headers=gem.headers())
result = request.json()

to_export: dict = \
    {'track~full': result['item'],
     'album~simplified': result.get('item').get('album'),
     'artist~simplified': result.get('item').get('artists')[0],
     'device~base': result.get('device'),
     'context~base': result.get('context')
     }

pickle_obj_map: dict = \
    {'track~full': music.Track,
     'album~simplified': music.Album,
     'artist~simplified': music.Artist,
     'device~base': device.Device,
     'context~base': context.Context
     }

fixture_src_dir = os.path.join(os.getcwd(), '_pytest_Fixture_src')

for obj_name, obj_dict in to_export.items():

    spot_obj = pickle_obj_map.get(obj_name)
    instantiated_obj = spot_obj(obj_dict)

    with open(
            os.path.join(fixture_src_dir, f'in_{obj_name}.pkl'),
            'wb') as f:
        pickle.dump(obj_dict, f)

    with open(os.path.join(fixture_src_dir, f'out_{obj_name}.pkl'),
              'wb') as f2:
        pickle.dump(instantiated_obj, f2)






music.Track(result.get('item'))
music.Artist(result.get('item').get('artists')[0])

with open(os.path.join(fixture_src_dir,
                       'activity_request_track.pkl'), 'wb') as f:
    pickle.dump(request, f)

with open(os.path.join(fixture_src_dir,
                       'activity_result_track.pkl'), 'wb') as f:
    pickle.dump(result, f)

with open(os.path.join(fixture_src_dir, 'device~base.pkl'), 'rb') as r:
    device_r = pickle.load(r)


from importlib import reload
from spotibot.core.objects import Device as device
reload(device)


test = device.Device(result['device'])

with open(os.path.join(fixture_src_dir, 'device~base~out.pkl'), 'wb') as w:
    pickle.dump(test, w)

with open(os.path.join(fixture_src_dir, 'device~base~out.pkl'), 'rb') as r:
    device_r2 = pickle.load(r)


vars(test) == vars(device_r2)


for k, v in test.validate().items():
    print(f"{k}:\n\t {v}")
    print(re.findall(r"class\s'(\w+)'", str(v.get('type'))))
    print('\n')

itemized_obj = vars(test)

vars(device.Device)

cnt_invalid = sum([1 for v in itemized_obj.values() if not v])
cnt_total = len(itemized_obj)

cnt_invalid
cnt_total

assert object_checker(test, device.Device)


len(vars(test))

for k, v in vars(test).items():
    print(k)