""" Fetch data from sources and dump to disk. """

import atexit
import json
import logging
import os
import time

from api import lastfm, pushbullet
from track import get_info as track_info

from config import (
    PB_PARAMS,
    PB_NOTIFY_WHEN,
    LOGGING_PARAMS,
    LFM_KEY,
    LFM_PAGES,
    LFM_PER_PAGE,
)


@atexit.register
def exit():
    """ Game Over. """
    PB_PARAMS['title'] = 'Finished: ' + PB_PARAMS['title']
    PB_PARAMS['body'] = PB_PARAMS['body'].format(count=count_files)
    pushbullet.send(**PB_PARAMS)

# Setup Logging
logging.basicConfig(**LOGGING_PARAMS)

# Folder to dump data to
folder = 'dump'
if not os.path.exists(folder):
    os.makedirs(folder)

# Keep track of files dumped
count_files = 0

# Let's get some data
for page in LFM_PAGES:
    r = lastfm.get(LFM_KEY, method='tag.getTopTracks', tag='electronic',
                   page=page, limit=LFM_PER_PAGE).json()

    if not r['tracks']['track']:
        PB_PARAMS['title'] = 'Null! - ' + PB_PARAMS['title']
        break

    for track in r['tracks']['track']:

        if track['name'] and track['artist']['name']:
            info = track_info(mbid=track['mbid'])

            # Dump data to disk!
            if info:
                data = {
                    'lfm': info[0],
                    'enest': info[1],
                }

                with open('%s/%s' % (folder, track['mbid']), 'w') as output:
                    json.dump(data, output)
                    count_files += 1

                    # Send progress to Pushbullet!
                    if (count_files % PB_NOTIFY_WHEN) == 0:
                        PB_PARAMS['body'] = PB_PARAMS['body'].format(count=count_files)
                        pushbullet.send(**PB_PARAMS)

        time.sleep(0.5)

    time.sleep(10)
