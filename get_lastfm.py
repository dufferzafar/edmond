from functools import partial
import tabulate
from api import lastfm

# Our data store
headers = ["Name", "MusicBrainz Identifier", "Duration"]
data = []

# A function that gets top tracks of a tag
tag_top = partial(lastfm.get, method='tag.getTopTracks')

# Let's get some data
for page in range(1, 2):
    r = tag_top(tag='electronic', page=page).json()

    for track in r['tracks']['track']:
        if track['mbid']:
            data.append([track['name'], track['mbid'], track['duration']])

print(tabulate.tabulate(data, headers=headers))
