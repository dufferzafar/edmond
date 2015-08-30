""" Fetch data from sources and dump to disk. """

import os
import json

from api import lastfm, pushbullet
from track import get_info as track_info

from config import (
    PB_PARAMS,
    PB_NOTIFY_WHEN,
)

# Folder to dump data to
folder = 'dump'
if not os.path.exists(folder):
    os.makedirs(folder)

# Keep track of files dumped
count_files = 0

# Let's get some data
for page in range(1, 2):
    r = lastfm.get(method='tag.getTopTracks', tag='electronic',
                   page=page, limit=5).json()

    for track in r['tracks']['track']:

        if track['mbid']:
            info = track_info(mbid=track['mbid'])

            # Dump data to disk!
            if info:
                data = {
                    'lfm': info[0],
                    'ab_high': info[1],
                    'ab_low': info[2],
                }

                with open('%s/%s' % (folder, track['mbid']), 'w') as output:
                    json.dump(data, output)
                    count_files += 1

                    # Send progress to Pushbullet!
                    if (count_files % PB_NOTIFY_WHEN) == 0:
                        PB_PARAMS['body'] = PB_PARAMS['body'].format(count=count_files)
                        pushbullet.send(**PB_PARAMS)

# Game Over!
PB_PARAMS['title'] = 'Finished: ' + PB_PARAMS['title']
PB_PARAMS['body'] = PB_PARAMS['body'].format(count=count_files)
pushbullet.send(**PB_PARAMS)
