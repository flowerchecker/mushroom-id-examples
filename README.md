# Mushroom-id-API

[Mushoom ID](https://www.kindwise.com/mushroom-id) is a mushroom identification API based on machine learning image recognition. [Get your API key](https://admin.kindwise.com/signup) and get started with your implementation.

 - **[documentation](https://mushroom.kindwise.com/docs)** - full API reference
 - **[python SDK](https://github.com/flowerchecker/kindwise-api-client)** - simply use API from pyhon 
 - API specification on **[Postman](https://www.postman.com/winter-shadow-932363/kindwise/collection/v0zjupf/mushroom-id)**
 - try [online demo](https://mushroom.kindwise.com/demo/)
 - more [python examples](python)

## Mushroom Identification 🍄
Send us your fungi images, and get a list of possible species suggestions with additional information.

```bash
pip install kindwise-api-client
```

```python
from kindwise import MushroomApi

api = MushroomApi('your_api_key')
identification = api.identify('../images/unknown_mushroom.jpg', details=['url', 'common_names'])

for suggestion in identification.result.classification.suggestions:
    print(suggestion.name)
    print(f'probability {suggestion.probability:.2%}')
    print(suggestion.details['url'])
    print(suggestion.details['common_names'])
    print()
```

Same example in pure python

```python
import base64
import requests

# encode images to base64
with open('unknown_mushroom.jpg', 'rb') as file:
    images = [base64.b64encode(file.read()).decode('ascii')]

response = requests.post(
    'https://mushroom.kindwise.com/api/v1/identification?details=common_names,url',
    json={
        'images': images,
        'similar_images': True,
    },
    headers={
        'Content-Type': 'application/json',
        'Api-Key': '-- ask for one: https://admin.kindwise.com/signup --',
    }).json()

for suggestion in response['result']['classification']['suggestions']:
    print(suggestion['name'])                     # Lactarius deterrimus
    print(suggestion['details']['common_names'])  # orange milkcap
    print(suggestion['details']['url'])           # https://en.wikipedia.org/wiki/Lactarius_deterrimus
```
