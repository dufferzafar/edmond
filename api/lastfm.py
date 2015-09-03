import requests

API_URL = 'http://ws.audioscrobbler.com/2.0/'


def get(API_KEY, **kwargs):
    """ Access any method of the last.fm webservice. """

    # Set up parameters
    params = dict(api_key=API_KEY, format='json', limit=100)
    params.update(kwargs)

    return requests.get(API_URL, params=params)
