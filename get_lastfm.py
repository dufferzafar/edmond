from functools import partial
from simplejson.scanner import JSONDecodeError

import tabulate

from api import lastfm, acousticbrainz

# Our data store
data = []
headers = [
    "Name",
    "MusicBrainz Identifier",
    "Duration",
    "Listeners",
    "Playcount",
    "AB - Female",
    "AB - Bright",
    "AB - Danceable",
    "AB - Voice",
]

# Get top tracks of a tag
tag_top = partial(lastfm.get, method='tag.getTopTracks')

# Get trak info
track_info = partial(lastfm.get, method='track.getInfo')

# Get high level information from Acousticbrainz
ab_high = acousticbrainz.get_high

# Let's get some data
for page in range(1, 2):
    r = tag_top(tag='electronic', page=page, limit=25).json()

    for track in r['tracks']['track']:
        if track['mbid']:
            info = track_info(mbid=track['mbid']).json()

            try:
                ab = ab_high(mbid=track['mbid'])
            except JSONDecodeError:
                continue

            data.append([
                track['name'],
                track['mbid'],
                info['track']['duration'],
                info['track']['listeners'],
                info['track']['playcount'],
                ab['female'],
                ab['bright'],
                ab['danceable'],
                ab['voice'],
            ])

print(tabulate.tabulate(data, headers=headers))
