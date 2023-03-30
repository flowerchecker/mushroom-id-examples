import base64
import requests
import os
import json
from urllib.parse import urlencode
from pathlib import Path


BASE_DIR = Path(__file__).parent.parent
API_KEY = os.environ.get('API_KEY', 'PUT_YOUR_API_KEY_HERE')


def encode_file(file_name):
    with open(file_name, 'rb') as file:
        return base64.b64encode(file.read()).decode('ascii')


def identify(file_names):
    # More optional parameters: https://github.com/flowerchecker/Mushroom-id-API/wiki/Request-identification
    payload = {
        'images': [encode_file(img) for img in file_names],
        'latitude': 49.1951239,
        'longitude': 16.6077111,
        'similar_images': True,
    }

    params = {
        # Details docs: https://github.com/flowerchecker/Mushroom-id-API/wiki/Details
        'details': 'common_names,gbif_id,taxonomy,rank,characteristic,edibility,psychoactive',
    }
    headers = {
        'Content-Type': 'application/json',
        'Api-Key': API_KEY,
    }

    response = requests.post(
        'https://mushroom.mlapi.ai/api/v1/identification?' + urlencode(params),
        json=payload,
        headers=headers,
    )

    assert response.status_code == 201, f'{response.status_code}: {response.text}'
    return response.json()


if __name__ == '__main__':
    identification = identify(
        [
            BASE_DIR / 'images' / 'example.jpg',
        ]
    )
    print(json.dumps(identification, indent=4))
