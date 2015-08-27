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
