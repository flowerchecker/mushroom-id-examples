# Mushroom-id-API
*⚠️ This service is in beta version and may undergo changes which may not be compatible with the current version.*

[Mushoom ID](https://web.plant.id/mushroom-id/) is a mushroom identification API based on machine learning image recognition. [Get your API key](https://admin.mlapi.ai/signup) and get started with your implementation.

See our **[documentation](http://mushroom.kindwise.com/docs)** for the full reference.

## Mushroom Identification 🍄
Send us your images of fungi encoded in base64, and you will receive a list of possible species suggestions with additional information.
```python
import base64
import requests

# encode images to base64
with open("unknown_mushroom.jpg", "rb") as file:
    images = [base64.b64encode(file.read()).decode("ascii")]

response = requests.post(
    "https://mushroom.mlapi.ai/api/v1/identification?details=common_names,url",
    json={
        "images": images,
        "similar_images": True,
    },
    headers={
        "Content-Type": "application/json",
        "Api-Key": "-- ask for one: https://admin.mlapi.ai/signup --",
    }).json()

for suggestion in response["result"]["classification"]["suggestions"]:
    print(suggestion["name"])                     # Lactarius deterrimus
    print(suggestion["details"]["common_names"])  # orange milkcap
    print(suggestion["details"]["url"])           # https://en.wikipedia.org/wiki/Lactarius_deterrimus
