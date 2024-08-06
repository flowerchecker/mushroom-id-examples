from kindwise import MushroomApi

api = MushroomApi('your_api_key')
identification = api.identify('../images/unknown_mushroom.jpg', details=['url', 'common_names'])

for suggestion in identification.result.classification.suggestions:
    print(suggestion.name)                              # Amanita muscaria
    print(f'probability {suggestion.probability:.2%}')  # probability 99.00%
    print(suggestion.details['url'])                    # https://en.wikipedia.org/wiki/Amanita_muscaria
    print(suggestion.details['common_names'])           # ['Fly agaric', 'Fly Amanita', 'Euro-Asian Fly Agaric']
    print()