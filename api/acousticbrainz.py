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
        acoustic=data['highlevel']['mood_acoustic']['all']['acoustic'],
        aggressive=data['highlevel']['mood_aggressive']['all']['aggressive'],
        danceable=data['highlevel']['danceability']['all']['danceable'],
        dortmund=data['highlevel']['genre_dortmund']['probability'],
        electronic=data['highlevel']['mood_electronic']['all']['electronic'],
        female=data['highlevel']['gender']['all']['female'],
        happy=data['highlevel']['mood_happy']['all']['happy'],
        party=data['highlevel']['mood_party']['all']['party'],
        relaxed=data['highlevel']['mood_relaxed']['all']['relaxed'],
        sad=data['highlevel']['mood_sad']['all']['sad'],
        timbre=data['highlevel']['timbre']['all']['bright'],
        tonal=data['highlevel']['tonal_atonal']['all']['tonal'],
        voice=data['highlevel']['voice_instrumental']['all']['voice'],
    )

    return rv

def get_low(mbid):
    """https://www.youtube.com/watch?v=12CeaxLiMgE"""
    data = get(mbid).json()

    rv = dict(
        average_loudness=data['lowlevel']['average_loudness'],
        barkbands_crest=data['lowlevel']['barkbands_crest']['mean'],
        barkbands_kurtosis=data['lowlevel']['barkbands_kurtosis']['mean'],
        barkbands_flatness_db=data['lowlevel']['barkbands_flatness_db']['mean'],
        barkbands_skewness=data['lowlevel']['barkbands_skewness']['mean'],
        barkbands_spread=data['lowlevel']['barkbands_spread']['mean'],
        dissonance=data['lowlevel']['dissonance']['mean'],
        dynamic_complexity=data['lowlevel']['dynamic_complexity'],
        erbbands_crest=data['lowlevel']['erbbands_crest']['mean'],
        erbbands_flatness_db=data['lowlevel']['erbbands_flatness_db']['mean'],
        erbbands_kurtosis=data['lowlevel']['erbbands_kurtosis']['mean'],
        erbbands_skewness=data['lowlevel']['erbbands_skewness']['mean'],
        erbbands_spread=data['lowlevel']['erbbands_spread']['mean'],
        hfc=data['lowlevel']['hfc']['mean'],
        melbands_crest=data['lowlevel']['melbands_crest']['mean'],
        melbands_flatness_db=data['lowlevel']['melbands_flatness_db']['mean'],
        melbands_kurtosis=data['lowlevel']['melbands_kurtosis']['mean'],
        melbands_skewness=data['lowlevel']['melbands_skewness']['mean'],
        melbands_spread=data['lowlevel']['melbands_spread']['mean'],
        pitch_salience=data['lowlevel']['pitch_salience']['mean'],
        silence_rate_30db=data['lowlevel']['silence_rate_30dB']['mean'],
        spectral_centroid=data['lowlevel']['spectral_centroid']['mean'],
        spectral_complexity=data['lowlevel']['spectral_complexity']['mean'],
        spectral_decrease=data['lowlevel']['spectral_decrease']['mean'],
        spectral_energy=data['lowlevel']['spectral_energy']['mean'],
        spectral_entropy=data['lowlevel']['spectral_entropy']['mean'],
        spectral_flux=data['lowlevel']['spectral_flux']['mean'],
        spectral_rms=data['lowlevel']['spectral_rms']['mean'],
        spectral_kurtosis=data['lowlevel']['spectral_kurtosis']['mean'],
        spectral_skewness=data['lowlevel']['spectral_skewness']['mean'],
        spectral_spread=data['lowlevel']['spectral_spread']['mean'],
        spectral_rolloff=data['lowlevel']['spectral_rolloff']['mean'],
        spectral_strongpeak=data['lowlevel']['spectral_strongpeak']['mean'],
        zerocrossingrate=data['lowlevel']['zerocrossingrate']['mean'],
    )

    return rv
