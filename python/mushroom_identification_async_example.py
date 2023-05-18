import base64
from time import sleep
import requests
import os
import json
from urllib.parse import urlencode
from pathlib import Path
import sys

BASE_DIR = Path(__file__).parent.parent
API_KEY = os.environ.get('API_KEY', 'PUT_YOUR_API_KEY_HERE')


def encode_file(file_name):
    with open(file_name, 'rb') as file:
        return base64.b64encode(file.read()).decode('ascii')


def create_identification(file_names):
    # More optional parameters: https://github.com/flowerchecker/Mushroom-id-API/wiki/Request-identification
    payload = {
        'images': [encode_file(img) for img in file_names],
        'latitude': 49.1951239,
        'longitude': 16.6077111,
        'similar_images': True,
    }
    headers = {
        'Content-Type': 'application/json',
        'Api-Key': API_KEY,
    }

    response = requests.post(
        'https://mushroom.mlapi.ai/api/v1/identification?async',
        json=payload,
        headers=headers,
    )

    assert response.status_code == 201, f'{response.status_code}: {response.text}'
    print(f'Identification URL: {response.headers["Location"]}', file=sys.stderr)
    return response.json()['access_token']


def get_completed_identification(access_token, tries=10):
    headers = {
        'Api-Key': API_KEY,
    }
    params = {
        # Details docs: https://github.com/flowerchecker/Mushroom-id-API/wiki/Details
        'details': 'common_names,gbif_id,taxonomy,rank,characteristic,edibility,psychoactive',
    }
    for _ in range(tries):
        print("Waiting for suggestions...", file=sys.stderr)
        sleep(1)
        response = requests.get(
            f'https://mushroom.mlapi.ai/api/v1/identification/{access_token}?' + urlencode(params),
            headers=headers,
        )
        assert response.status_code == 200, f'{response.status_code}: {response.text}'
        identification = response.json()
        assert identification['status'] != 'FAILED', f'The identification {access_token} failed.'
        if identification['status'] == 'COMPLETED':
            return identification
    assert False, f'Cannot retrieve result for identification {access_token}.'


if __name__ == '__main__':
    access_token = create_identification(
        [
            BASE_DIR / 'images' / 'example.jpg',
        ]
    )
    identification = get_completed_identification(access_token)
    print(json.dumps(identification, indent=4))
