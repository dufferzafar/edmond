""" Fetch data from sources and dump to disk. """

import os
from functools import partial

import json

from api import lastfm
from track import get_info as track_info

folder = 'dump'
if not os.path.exists(folder):
    os.makedirs(folder)

# Get top tracks of a tag
tag_top = partial(lastfm.get, method='tag.getTopTracks')

# Let's get some data
for page in range(1, 2):
    r = tag_top(tag='electronic', page=page, limit=10).json()

    for track in r['tracks']['track']:

        if track['mbid']:
            info = track_info(mbid=track['mbid'])

            # Dump data to disk!
            if info:
                with open('%s/%s' % (folder, track['mbid']), 'w') as output:
                    json.dump({'lfm': info[0], 'ab_high': info[1], 'ab_low': info[2]}, output)
