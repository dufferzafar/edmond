from api import lastfm, echonest
from config import LFM_KEY, EN_KEY


def get_info(mbid):
    """ Fetch track information from multiple sources. """
    try:
        lfm = lastfm.get(LFM_KEY, method='track.getInfo', mbid=mbid).json()
        en = echonest.get(EN_KEY,
                          title=lfm['track']['name'],
                          artist=lfm['track']['artist']['name'])

        if not en['track']['audio_summary']:
            raise ValueError

    except ValueError:
        # TODO: What if a song is on last.fm but not on EN?
        return None

    return (lfm, en)


def features(lfm, en):
    """ Build features dictionary. """

    rv = {
        # Last.fm
        "Name": lfm['track']['name'],
        "Artist": lfm['track']['artist']['name'],
        "MBID": lfm['track']['mbid'],
        "Duration": lfm['track']['duration'],
        "Listeners": lfm['track']['listeners'],
        "Playcount": lfm['track']['playcount'],

        # EchoNest
        "Time_Singature": en['track']['audio_summary']['time_signature'],
        "Loudness": en['track']['audio_summary']['loudness'],
    }

    return rv

# TODO: Figure out a way to avoid listing this
# Currently required to order the columns of the dataframe
feature_list = ["Name", "Artist", "MBID", "Listeners",
                "Playcount", "Duration", "Time Singature", "Loudness"]

if __name__ == '__main__':
    print(get_info(mbid="c741a7ef-dd33-4c79-a4d4-8745d9675620"))
