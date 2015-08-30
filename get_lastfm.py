from functools import partial

from api import lastfm
from track import get_info as track_info

# Our data store
data = []

# Get top tracks of a tag
tag_top = partial(lastfm.get, method='tag.getTopTracks')

# Let's get some data
for page in range(1, 2):
    r = tag_top(tag='electronic', page=page, limit=5).json()
    for track in r['tracks']['track']:
        if track['mbid']:
            info = track_info(mbid=track['mbid'])
            if info:
                data.append(info)

