import requests


# Search mushroom knowledge base by query. Entities are searchable by scientific names, common names (in specified language), synonyms.
# Plant name and query are always matched from start of a word., i.e. "Aloe vera" is searchable by "Aloe", "Alo", "Vera", "ver", "Aloe vera"...


mushroom_for_search = 'amanita'
limit = 3 # int (optional) - maximum of returned result, max. 20, default 10
language = 'en' # two-letter ISO 639-1 language code (optional, default en) - language of common names can be multiple (up to 3), separated by comma - i.e. (en,de,sv)

response = requests.get(
    'https://mushroom.kindwise.com/api/v1/kb/mushroom/name_search',
    params={'q': mushroom_for_search, 'limit': limit, 'lang': language},
    headers={'Api-Key': 'your_api_key'},
)

search = response.json()
print(search) # {'entities': [{'matched_in': 'Amanita muscaria', 'matched_in_type': 'entity_name', 'access_token': 'bVhGdgozEHVoWXNCVzVHcXdCUGgfek92VGxXMVtrYlE-', 'match_position': 0, 'match_length': 7, 'entity_name': 'Amanita muscaria'}, {'matched_in': 'Amanita persicina', 'matched_in_type': 'entity_name', 'access_token': 'PVhGdgczQHVpWXVCAzUTcXZCWGgfekR2DmxVMVJrYFE-', 'match_position': 0, 'match_length': 7, 'entity_name': 'Amanita persicina'}, {'matched_in': 'Amanita rubescens', 'matched_in_type': 'entity_name', 'access_token': 'OVhCdgQzR3U_WXNCVjVJcXRCC2hNekV2D2xVMQ1rMFE-', 'match_position': 0, 'match_length': 7, 'entity_name': 'Amanita rubescens'}], 'entities_trimmed': True, 'limit': 3}


# Get entity details based on access token from Mushroom search endpoint.
# One call cost 0.5 credits.

if search['entities']:
    access_token = search['entities'][0]['access_token']
    requested_mushroom_details = 'common_names,url,description,edibility,image'
    # comma separetad list of requested mushroom details (required) see detail description in documentation (http://mushroom.kindwise.com/docs)

    response = requests.get(
        f'https://mushroom.kindwise.com/api/v1/kb/mushroom/{access_token}',
        params={'details': requested_mushroom_details, 'lang': language},
        headers={'Api-Key': 'your_api_key'},
    )

    detail = response.json()
    print(detail) # {'common_names': ['Fly agaric', 'Fly Amanita', 'Euro-Asian Fly Agaric'], 'url': 'https://en.wikipedia.org/wiki/Amanita_muscaria', 'edibility': 'poisonous', 'description': {'value': "Amanita muscaria, commonly known as the fly agaric or fly amanita, is a basidiomycete of the genus Amanita. It is also a muscimol mushroom. Native throughout the temperate and boreal regions of the Northern Hemisphere, Amanita muscaria has been unintentionally introduced to many countries in the Southern Hemisphere, generally as a symbiont with pine and birch plantations, and is now a true cosmopolitan species. It associates with various deciduous and coniferous trees.\nArguably the most iconic toadstool species, the fly agaric is a large white-gilled, white-spotted, usually red mushroom, and is one of the most recognizable and widely encountered in popular culture, including in video games—e.g., the extensive use of a recognizable Amanita muscaria in the Mario franchise and its Super Mushroom power-up—and television—e.g., the houses in The Smurfs franchise.Despite its easily distinguishable features, Amanita muscaria is a fungus with several known variations, or subspecies. These subspecies are slightly different, some having yellow or white caps, but they are all usually called fly agarics, and they are most of the time recognizable by their notable white spots. Recent DNA fungi research, however, has shown that some of these variations are not the same species at all, such as the peach-colored fly agaric (Amanita persicina) for example, but the common name 'fly agaric' clings on.\nAlthough poisonous, death due to poisoning from A. muscaria ingestion is quite rare. Parboiling twice with water draining weakens its toxicity and breaks down the mushroom's psychoactive substances; it is eaten in parts of Europe, Asia, and North America. All Amanita muscaria varieties, but in particular A. muscaria var. muscaria, are noted for their hallucinogenic properties, with the main psychoactive constituents being muscimol and its neurotoxic precursor ibotenic acid. A local variety of the mushroom was used as an intoxicant and entheogen by the indigenous peoples of Siberia.\n\n", 'citation': 'https://en.wikipedia.org/wiki/Amanita_muscaria', 'license_name': 'CC BY-SA 3.0', 'license_url': 'https://creativecommons.org/licenses/by-sa/3.0/'}, 'image': {'value': 'https://mushroom-id.ams3.cdn.digitaloceanspaces.com/knowledge_base/wikidata/2eb/2ebad87c493137cc89d68c6c3df3bb892e0a81d2.jpg', 'citation': '//commons.wikimedia.org/wiki/User:Onderwijsgek', 'license_name': 'CC BY-SA 3.0', 'license_url': 'https://creativecommons.org/licenses/by-sa/3.0/'}, 'language': 'en', 'entity_id': '509e11b658e98f03', 'name': 'Amanita muscaria'}
