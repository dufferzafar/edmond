import pyen


def get(enest_key, title, artist):
    en = pyen.Pyen(enest_key)

    id_response = en.get('song/search', title=title, artist=artist)
    song_id = id_response['songs'][0]['id']
    feature_response = en.get('track/profile', id=song_id, bucket='audio_summary')

    return feature_response
