from api import lastfm, echonest
from config import LFM_KEY, ENEST_KEY


def get_info(mbid, songname, artist):
    """ Fetch track information from multiple sources. """
    try:
        # Last.fm
        lfm = lastfm.get(LFM_KEY, method='track.getInfo', mbid=mbid).json()
        # Echonest
        enest = echonest.get(ENEST_KEY).json()
    except ValueError:
        # TODO: What if a song is on last.fm but not on AB?
        return None

    return (lfm,enest)


def features(lfm, enest):
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
        "Time_Singature" : enest['track']['audio_summary']['time_signature'],
        "Loudness" : enest['track']['audio_summary']['loudness'],

        # AcousticBrainz High Level Data
        # "ABH - Acoustic": ab_high['highlevel']['mood_acoustic']['all']['acoustic'],
        # "ABH - Aggressive": ab_high['highlevel']['mood_aggressive']['all']['aggressive'],
        # "ABH - Danceable": ab_high['highlevel']['danceability']['all']['danceable'],
        # "ABH - Dortmund": ab_high['highlevel']['genre_dortmund']['probability'],
        # "ABH - Electronic": ab_high['highlevel']['mood_electronic']['all']['electronic'],
        # "ABH - Female": ab_high['highlevel']['gender']['all']['female'],
        # "ABH - Happy": ab_high['highlevel']['mood_happy']['all']['happy'],
        # "ABH - Party": ab_high['highlevel']['mood_party']['all']['party'],
        # "ABH - Relaxed": ab_high['highlevel']['mood_relaxed']['all']['relaxed'],
        # "ABH - Sad": ab_high['highlevel']['mood_sad']['all']['sad'],
        # "ABH - Timbre": ab_high['highlevel']['timbre']['all']['bright'],
        # "ABH - Tonal": ab_high['highlevel']['tonal_atonal']['all']['tonal'],
        # "ABH - Voice": ab_high['highlevel']['voice_instrumental']['all']['voice'],

        # AcousticBrainz Low Level Data
        # "ABL - Average Loudness": ab_low['lowlevel']['average_loudness'],
        # "ABL - Barkbands Crest": ab_low['lowlevel']['barkbands_crest']['mean'],
        # "ABL - Barkbands Kurtosis": ab_low['lowlevel']['barkbands_kurtosis']['mean'],
        # "ABL - Barkbands Flatness dB": ab_low['lowlevel']['barkbands_flatness_db']['mean'],
        # "ABL - Barkbands Skewness": ab_low['lowlevel']['barkbands_skewness']['mean'],
        # "ABL - Barkbands Spread": ab_low['lowlevel']['barkbands_spread']['mean'],
        # "ABL - Dissonance": ab_low['lowlevel']['dissonance']['mean'],
        # "ABL - Dynamic Complexity": ab_low['lowlevel']['dynamic_complexity'],
        # "ABL - Erbbands Crest": ab_low['lowlevel']['erbbands_crest']['mean'],
        # "ABL - Erbbands Flatness dB": ab_low['lowlevel']['erbbands_flatness_db']['mean'],
        # "ABL - Erbbands Kurtosis": ab_low['lowlevel']['erbbands_kurtosis']['mean'],
        # "ABL - Erbbands Skewness": ab_low['lowlevel']['erbbands_skewness']['mean'],
        # "ABL - Erbbands Spread": ab_low['lowlevel']['erbbands_spread']['mean'],
        # "ABL - HFC": ab_low['lowlevel']['hfc']['mean'],
        # "ABL - Melbands Crest": ab_low['lowlevel']['melbands_crest']['mean'],
        # "ABL - Melbands Flatness dB": ab_low['lowlevel']['melbands_flatness_db']['mean'],
        # "ABL - Melbands Kurtosis": ab_low['lowlevel']['melbands_kurtosis']['mean'],
        # "ABL - Melbands Skewness": ab_low['lowlevel']['melbands_skewness']['mean'],
        # "ABL - Melbands Spread": ab_low['lowlevel']['melbands_spread']['mean'],
        # "ABL - Pitch Salience": ab_low['lowlevel']['pitch_salience']['mean'],
        # "ABL - Silence Rate 30dB": ab_low['lowlevel']['silence_rate_30dB']['mean'],
        # "ABL - Spectral Centroid": ab_low['lowlevel']['spectral_centroid']['mean'],
        # "ABL - Spectral Complexity": ab_low['lowlevel']['spectral_complexity']['mean'],
        # "ABL - Spectral Decrease": ab_low['lowlevel']['spectral_decrease']['mean'],
        # "ABL - Spectral Energy": ab_low['lowlevel']['spectral_energy']['mean'],
        # "ABL - Spectral Entropy": ab_low['lowlevel']['spectral_entropy']['mean'],
        # "ABL - Spectral Flux": ab_low['lowlevel']['spectral_flux']['mean'],
        # "ABL - Spectral RMS": ab_low['lowlevel']['spectral_rms']['mean'],
        # "ABL - Spectral Kurtosis": ab_low['lowlevel']['spectral_kurtosis']['mean'],
        # "ABL - Spectral Skewness": ab_low['lowlevel']['spectral_skewness']['mean'],
        # "ABL - Spectral Spread": ab_low['lowlevel']['spectral_spread']['mean'],
        # "ABL - Spectral Rolloff": ab_low['lowlevel']['spectral_rolloff']['mean'],
        # "ABL - Spectral Strongpeak": ab_low['lowlevel']['spectral_strongpeak']['mean'],
        # "ABL - Zero Crossing Rate": ab_low['lowlevel']['zerocrossingrate']['mean'],
    }

    return rv

# TODO: Figure out a way to avoid listing this
# Currently required to order the columns of the dataframe
# feature_list = ["Name", "Artist", "MBID", "Listeners", "Playcount", "Duration", "ABH - Acoustic", "ABH - Aggressive", "ABH - Danceable", "ABH - Dortmund", "ABH - Electronic", "ABH - Female", "ABH - Happy", "ABH - Party", "ABH - Relaxed", "ABH - Sad", "ABH - Timbre", "ABH - Tonal", "ABH - Voice", "ABL - Average Loudness", "ABL - Barkbands Crest", "ABL - Barkbands Kurtosis", "ABL - Barkbands Flatness dB", "ABL - Barkbands Skewness", "ABL - Barkbands Spread", "ABL - Dissonance", "ABL - Dynamic Complexity", "ABL - Erbbands Crest", "ABL - Erbbands Flatness dB", "ABL - Erbbands Kurtosis", "ABL - Erbbands Skewness", "ABL - Erbbands Spread", "ABL - HFC", "ABL - Melbands Crest", "ABL - Melbands Flatness dB", "ABL - Melbands Kurtosis", "ABL - Melbands Skewness", "ABL - Melbands Spread", "ABL - Pitch Salience", "ABL - Silence Rate 30dB", "ABL - Spectral Centroid", "ABL - Spectral Complexity", "ABL - Spectral Decrease", "ABL - Spectral Energy", "ABL - Spectral Entropy", "ABL - Spectral Flux", "ABL - Spectral RMS", "ABL - Spectral Kurtosis", "ABL - Spectral Skewness", "ABL - Spectral Spread", "ABL - Spectral Rolloff", "ABL - Spectral Strongpeak", "ABL - Zero Crossing Rate"]

feature_list = ["Name", "Artist", "MBID", "Listeners", "Playcount", "Duration", "Time Singature", "Loudness"]

if __name__ == '__main__':
    print(get_info(mbid="c741a7ef-dd33-4c79-a4d4-8745d9675620"))
