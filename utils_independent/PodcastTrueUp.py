

from spotibot.core.objects import User as user

import requests
import os
import pandas as pd
import time

gem = user.UserDBO('125393293')

# Getting historical episode ID(s) --------------------------------------------
href_existing = r'https://api.spotify.com/v1/playlists/' \
                r'4RKIVPzUpCbG2YJuI2Nrfv/tracks'

request_existing = requests.get(href_existing, headers=gem.headers())
result_existing = request_existing.json()

existing_ids = \
    [val.get('track').get('id') for val in result_existing.get('items')]

existing_ids

# Reading in batched ID(s) ----------------------------------------------------

path_to_excel = \
    os.path.join(os.getcwd(), 'sandbox', 'Podcast URIs To Add.xlsx')

df = pd.read_excel(path_to_excel, header=None)

to_add_uri = [val.split(':')[-1] for val in df[0]]

# Combining all ID(s) ---------------------------------------------------------
all_uri = to_add_uri + existing_ids
all_uri = [val for val in set(all_uri)]
# TODO: Add URI(s) from existing currently played episodes as well

# Batching - successful API comms but not returning full array of episodes-----


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


chunked = chunks(all_uri, 50)

href = r'https://api.spotify.com/v1/episodes'

results = []
while chunked:
    data = {'ids': next(chunked)}
    request2 = requests.get(href, params=data, headers=gem.headers())
    result2 = request2.json()
    results.append(result2)

# Single request per episode---------------------------------------------------

results = []
for i, uri in enumerate(all_uri):
    href2 = f'https://api.spotify.com/v1/episodes/{uri}'
    request = requests.get(href2, headers=gem.headers())
    result = request.json()
    results.append(result)
    print(f"<{i}> completed")
    time.sleep(1)

episode_dict = {k.get('id'): k.get('release_date') for k in results}

date_uri_dict = {v: [] for v in episode_dict.values()}

for k, v in episode_dict.items():
    subber = date_uri_dict.get(v)
    subber.append(k)
# TODO: Add these URIs to the all podcasts played playlist in cronological
#  order (oldest gets added first)
