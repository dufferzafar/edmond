import pyen

def get():
	en = pyen.Pyen("HCMA5DHVIH502MXH1")
	id_response = en.get('song/search', title='my iron lung', artist='radiohead')

	song_id = id_response['songs'][0]['id']

	feature_response = en.get('track/profile', id=song_id, bucket='audio_summary')

	return feature_response

# if feature_response['track']['audio_summary']:
# 	time_sign = feature_response['track']['audio_summary']['time_signature']
# 	duration = feature_response['track']['audio_summary']['song_duration']
# 	loudness = feature_response['track']['audio_summary']['loudness']
