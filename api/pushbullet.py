import json
import requests

PB_URL = 'https://api.pushbullet.com/v2/pushes'


def send(token, title, body, source=None, target=None):
    """ Send a note to pushbullet. """

    data = {
        "type": "note",
        "title": title,
        "body": body,
        "source_device_iden": source,
        "device_iden": target,
    }

    headers = {'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json'}
    resp = requests.post(PB_URL, data=json.dumps(data), headers=headers)

    return resp
