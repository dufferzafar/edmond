import requests

API_URL = 'http://ws.audioscrobbler.com/2.0/'
API_KEY = '1e3f5c62ae6ea96b97fd4d4e00f4825a'


def get(**kwargs):
    """ Access any method of the last.fm webservice. """

    # Set up parameters
    params = dict(api_key=API_KEY, format='json', limit=100)
    params.update(kwargs)

    return requests.get(API_URL, params=params)
