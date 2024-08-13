from datetime import datetime

from kindwise import MushroomApi

if __name__ == '__main__':
    api = MushroomApi('your_api_key')
    identification = api.identify(
        ['../images/photo_1.jpg', '../images/photo_2.jpg'],
        latitude_longitude=(13.3966042, 23.3150361),
        date_time=datetime(2024, 8, 13),
        details=[
            'common_names',     # list of strings - localized - local, non-scientific name
            'url',              # string - localized - link to mushroom profile page (usually Wikipedia); if localized page not available, an English one is provided
            'description',      # string - localized, licensed - short description from Wikipedia
            'edibility',        # string - one of
                                    # choice: highly regarded for its edibility and widely used in cooking
                                    # edible: safe to eat
                                    # edible when cooked: only edible when cooked
                                    # caution: there are warnings regarding the mushroom’s edibility, such as stomach irritations or easy confusion with poisonous mushroom species
                                    # medicinal: valued for its medicinal properties
                                    # inedible: not considered edible
                                    # poisonous: toxic and should not be eaten
                                    # deadly: can cause fatal poisoning
            'psychoactive',     # bool - this mushroom causes poisoning that affects the nervous system
            'characteristic',   # dict - possible values are the following: hymenium attachment, hymenium type, mushroom cap shape, mushroom ecological type, spore print color, stipe character
            'look_alike',       # list of dicts - mushrooms that are frequently confused with the suggested species; each taxon contains entity_id, name and url
            'taxonomy',         # dict - scientific taxonomy
            'rank',             # string - taxonomic rank
            'gbif_id',          # int - id in GBIF database
            'inaturalist_id',   # int - id in iNaturalist database
            'image',            # string - with licence - url of representative image
            'images'            # list - with licences - list of more urls of representative images
        ],
        language='de',
        similar_images=True,
    )

    for suggestion in identification.result.classification.suggestions:
        print(suggestion.name)
        print(f'probability {suggestion.probability:.2%}')
        print(suggestion.details)
        print(suggestion.similar_images)
        print()
