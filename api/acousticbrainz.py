import requests

API_URL = 'http://acousticbrainz.org/{mbid}/{level}'


def get(mbid, level='low', n=0):
    """
    Get acoustic information for a recording mbid.

    level can be 'low' or 'high'
    n is the document number to fetch.

    http://acousticbrainz.org/96685213-a25c-4678-9a13-abd9ec81cf35/low-level?n=1
    """

    # Todo: /count/ ?

    # Set up URL
    url = API_URL.format(mbid=mbid, level=level+'-level')

    return requests.get(url, params=dict(n=n))


def get_high(mbid):
    """Get the high level dictionary from acousticbrainz data. """
    data = get(mbid, level='high').json()

    rv = dict(
        female=data['highlevel']['gender']['all']['female'],
        bright=data['highlevel']['timbre']['all']['bright'],
        danceable=data['highlevel']['danceability']['all']['danceable'],
        voice=data['highlevel']['voice_instrumental']['all']['voice'],
    )

    return rv
