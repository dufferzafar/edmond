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
        acoustic=data['highlevel']['mood_acoustic']['acoustic'],
        aggressive=data['highlevel']['mood_aggressive']['aggressive'],
        danceable=data['highlevel']['danceability']['all']['danceable'],
        dortmund=data['highlevel']['genre_dortmund']['probability'],
        electronic=data['highlevel']['mood_electronic']['electronic'],
        female=data['highlevel']['gender']['all']['female'],
        happy=data['highlevel']['mood_happy']['happy'],
        party=data['highlevel']['mood_party']['party'],
        relaxed=data['highlevel']['mood_relaxed']['relaxed'],
        sad=data['highlevel']['mood_sad']['sad'],
        timbre=data['highlevel']['timbre']['all']['bright'],
        tonal=data['highlevel']['tonal_atonal']['all']['tonal'],
        voice=data['highlevel']['voice_instrumental']['all']['voice'],
    )

    return rv

def get_low(mbid):
    """https://www.youtube.com/watch?v=12CeaxLiMgE"""
    data = get(mbid).json()

    rv = dict(
        average_loudness=['lowlevel']['average_loudness'],
        barkbands_crest=['lowlevel']['barkbands_crest']['mean'],
        barkbands_kurtosis=['lowlevel']['barkbands_kurtosis']['mean'],
        barkbands_flatness_db=['lowlevel']['barkbands_skewnessnds_flatness_db']['mean'],
        barkbands_skewness=['lowlevel']['barkbands_skewness']['mean'],
        barkbands_spread=['lowlevel']['barkbands_spread']['mean'],
        dissonance=['lowlevel']['dissonance']['mean'],
        dynamic_complexity=['lowlevel']['dynamic_complexity'],
        errbands_crest=['lowlevel']['errbands_crest']['mean'],
        errbands_flatness_db=['lowlevel']['errbands_flatness_db']['mean'],
        errbands_kurtosis=['lowlevel']['errbands_kurtosis']['mean'],
        errbands_skewness=['lowlevel']['errbands_skewness']['mean'],
        errbands_spread=['lowlevel']['errbands_spread']['mean'],
        hfc=['lowlevel']['hfc']['mean'],
        melbands_crest=['lowlevel']['melbands_crest']['mean'],
        melbands_flatness_db=['lowlevel']['melbands_flatness_db']['mean'],
        melbands_kurtosis=['lowlevel']['melbands_kurtosis']['mean'],
        melbands_skewness=['lowlevel']['melbands_skewness']['mean'],
        melbands_spread=['lowlevel']['melbands_spread']['mean'],
        pitch_salience=['lowlevel']['pitch_salience']['mean'],
        silence_rate_30db=['lowlevel']['silence_rate_30db']['mean'],
        spectral_centroid=['lowlevel']['spectral_centroid']['mean'],
        spectral_complexity=['lowlevel']['spectral_complexity']['mean'],
        spectral_decrease=['lowlevel']['spectral_decrease']['mean'],
        spectral_energy=['lowlevel']['spectral_energy']['mean'],
        spectral_entropy=['lowlevel']['spectral_entropy']['mean'],
        spectral_flux=['lowlevel']['spectral_flux']['mean'],
        spectral_rms=['lowlevel']['spectral_rms']['mean'],
        spectral_kurtosis=['lowlevel']['spectral_kurtosis']['mean'],
        spectral_skewness=['lowlevel']['spectral_skewness']['mean'],
        spectral_spread=['lowlevel']['spectral_spread']['mean'],
        spectral_rolloff=['lowlevel']['spectral_rolloff']['mean'],
        spectral_strongpeak=['lowlevel']['spectral_strongpeak']['mean'],
        zerocrossingrate=['lowlevel']['zerocrossingrate']['mean'],
    )

    return rv
