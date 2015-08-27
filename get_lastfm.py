from functools import partial
import tabulate
from api import lastfm

# Our data store
data = []
headers = [
    "Name",
    "MusicBrainz Identifier",
    "Duration",
    "Listeners",
    "Playcount",
]

# Get top tracks of a tag
tag_top = partial(lastfm.get, method='tag.getTopTracks')

# Get trak info
track_info = partial(lastfm.get, method='track.getInfo')

# Let's get some data
for page in range(1, 2):
    r = tag_top(tag='electronic', page=page, limit=25).json()

    for track in r['tracks']['track']:
        if track['mbid']:
            info = track_info(mbid=track['mbid']).json()
            data.append([
                track['name'],
                track['mbid'],
                info['track']['duration'],
                info['track']['listeners'],
                info['track']['playcount'],
            ])

print(tabulate.tabulate(data, headers=headers))
