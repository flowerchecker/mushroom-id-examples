import base64

import requests

with open('../images/unknown_mushroom.jpg', 'rb') as file:
    images = [base64.b64encode(file.read()).decode('ascii')]

response = requests.post(
    'https://mushroom.kindwise.com/api/v1/identification',
    params={'details': 'common_names,gbif_id,taxonomy,rank,characteristic,edibility,psychoactive'},
    headers={'Api-Key': 'your_api_key'},
    json={'images': images},
)

identification = response.json()
print(identification)
for suggestion in identification['result']['classification']['suggestions']:
    print(suggestion['name'])                               # Amanita muscaria
    print(f'probability {suggestion["probability"]:.2%}')   # 0.99
    print(suggestion['details']['common_names'])            # ['Fly agaric', 'Fly Amanita', 'Euro-Asian Fly Agaric']
    print()
