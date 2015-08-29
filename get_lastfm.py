from functools import partial
from simplejson.scanner import JSONDecodeError

import tabulate

from api import lastfm, acousticbrainz

# Our data store
data = []
headers = [
    "Name",
    "MusicBrainz Identifier",
    "Duration",
    "Listeners",
    "Playcount",
    "AB - Acoustic",
    "AB - Aggressive",
    "AB - Danceable",
    "AB - Dortmund",
    "AB - Electronic",
    "AB - Female",
    "AB - Happy",
    "AB - Party",
    "AB - Relaxed",
    "AB - Sad",
    "AB - Timbre",
    "AB - Tonal",
    "AB - Voice",
    "AB - Average Loudness",
    "AB - Barkbands Crest",
    "AB - Barkbands Kurtosis",
    "AB - Barkbands Flatness dB",
    "AB - Barkbands Skewness",
    "AB - Barkbands Spread",
    "AB - Dissonance",
    "AB - Dynamic Complexity",
    "AB - Errbands Crest",
    "AB - Errbands Flatness dB",
    "AB - Errbands Kurtosis",
    "AB - Errbands Skewness",
    "AB - Errbands Spread",
    "AB - HFC",
    "AB - Melbands Crest",
    "AB - Melbands Flatness dB",
    "AB - Melbands Kurtosis",
    "AB - Melbands Skewness",
    "AB - Melbands Spread",
    "AB - Pitch Salience",
    "AB - Silence Rate 30dB",
    "AB - Spectral Centroid",
    "AB - Spectral Complexity",
    "AB - Spectral Decrease",
    "AB - Spectral Energy",
    "AB - Spectral Entropy",
    "AB - Spectral Flux",
    "AB - Spectral RMS",
    "AB - Spectral Kurtosis",
    "AB - Spectral Skewness",
    "AB - Spectral Spread",
    "AB - Spectral Rolloff",
    "AB - Spectral Strongpeak",
    "AB - Zero Crossing Rate",
]


# Get top tracks of a tag
tag_top = partial(lastfm.get, method='tag.getTopTracks')

# Get trak info
track_info = partial(lastfm.get, method='track.getInfo')

# Get high level information from Acousticbrainz
ab_high = acousticbrainz.get_high

ab_low = acousticbrainz.get_low

# Let's get some data
for page in range(1, 2):
    r = tag_top(tag='electronic', page=page, limit=25).json()

    for track in r['tracks']['track']:
        if track['mbid']:
            info = track_info(mbid=track['mbid']).json()

            try:
                # 1 is high, 0 is low. Binary basics, people!
                ab1 = ab_high(mbid=track['mbid'])
                ab0 = ab_low(mbid=track['mbid'])
            except JSONDecodeError:
                continue

            data.append([
                track['name'],
                track['mbid'],
                info['track']['duration'],
                info['track']['listeners'],
                info['track']['playcount'],
                ab1['acoustic'],
                ab1['aggressive'],
                ab1['danceable'],
                ab1['dortmund'],
                ab1['electronic'],
                ab1['female'],
                ab1['happy'],
                ab1['party'],
                ab1['relaxed'],
                ab1['sad'],
                ab1['timbre'],
                ab1['tonal'],
                ab1['voice'],
                ab0['average_loudness'],
                ab0['barkbands_crest'],
                ab0['barkbands_kurtosis'],
                ab0['barkbands_flatness_db'],
                ab0['barkbands_skewness'],
                ab0['barkbands_spread'],
                ab0['dissonance'],
                ab0['dynamic_complexity'],
                ab0['errbands_crest'],
                ab0['errbands_flatness_db'],
                ab0['errbands_kurtosis'],
                ab0['errbands_skewness'],
                ab0['errbands_spread'],
                ab0['hfc'],
                ab0['melbands_crest'],
                ab0['melbands_flatness_db'],
                ab0['melbands_kurtosis'],
                ab0['melbands_skewness'],
                ab0['melbands_spread'],
                ab0['pitch_salience'],
                ab0['silence_rate_30db'],
                ab0['spectral_centroid'],
                ab0['spectral_complexity'],
                ab0['spectral_decrease'],
                ab0['spectral_energy'],
                ab0['spectral_entropy'],
                ab0['spectral_flux'],
                ab0['spectral_rms'],
                ab0['spectral_kurtosis'],
                ab0['spectral_skewness'],
                ab0['spectral_spread'],
                ab0['spectral_rolloff'],
                ab0['spectral_strongpeak'],
                ab0['zerocrossingrate'],
            ])

print(tabulate.tabulate(data, headers=headers))