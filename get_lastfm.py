from functools import partial
from simplejson.scanner import JSONDecodeError

import tabulate

from api import lastfm, acousticbrainz

# Our data store
data = []

# Get top tracks of a tag
tag_top = partial(lastfm.get, method='tag.getTopTracks')

# Let's get some data
for page in range(1, 2):
    r = tag_top(tag='electronic', page=page, limit=25).json()

    for track in r['tracks']['track']:
        if track['mbid']:
            info = track_info(mbid=track['mbid']).json()

print(tabulate.tabulate(data, headers=headers))