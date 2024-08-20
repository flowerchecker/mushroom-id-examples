from kindwise import MushroomApi, SearchResult


# Search mushroom knowledge base by query. Entities are searchable by scientific names, common names (in specified
# language), synonyms. Mushroom name and query are always matched from start of a word., i.e. "Amanita muscaria" is
# searchable by "Amanita", "Amanit", "muscaria", "muscari", "Amanita muscaria"...

api = MushroomApi('your_api_key')

mushroom_for_search = 'amanita'
limit = 3        # int (optional) - maximum of returned result, max. 20, default 10
language = 'de'  # two-letter ISO 639-1 language code (optional, default en) - language of common names can be
# multiple (up to 3), separated by comma - i.e. (en,de,sv)
search_result: SearchResult = api.search(mushroom_for_search, language=language, limit=limit)

print(search_result)    # SearchResult(entities=[SearchEntity(matched_in='Amanita muscaria',
# matched_in_type='entity_name', access_token='YVRRYVtiHXgDMnNCFnR1Q0N2aFAzVlxlfUU2UFVlWWo-', match_position=0,
# match_length=7), SearchEntity(matched_in='Amanita persicina', matched_in_type='entity_name',
# access_token='MVRRYVZiTXgCMnVCQnQhQ0J2YFAzVldlJ0U0UFxlW2o-', match_position=0, match_length=7), SearchEntity(
# matched_in='Amanita rubescens', matched_in_type='entity_name',
# access_token='NVRVYVViSnhUMnNCF3R7Q0B2M1BhVlZlJkU0UANlC2o-', match_position=0, match_length=7)],
# entities_trimmed=True, limit=3)


# Get entity details based on access token from Mushroom search endpoint.
# One call cost 0.5 credits.

access_token = search_result.entities[0].access_token
requested_mushroom_details = 'common_names,url,description,edibility,image'
# comma separetad list of requested mushroom details (required) see detail description in documentation (
# https://mushroom.kindwise.com/docs)

entity_details = api.get_kb_detail(access_token, requested_mushroom_details, language=language)
print(entity_details)   # {'common_names': ['Fliegenpilz', 'Roter Fliegenpilz', 'Mückenschwamm', 'Mückenpfeffer',
# 'Fliegenschwamm', 'Fliegenteufel', 'Sunneschirmche', 'Bunte Poggenstool', 'Narrenschwamm', 'Krötenstuhl'],
# 'url': 'https://de.wikipedia.org/wiki/Fliegenpilz', 'edibility': 'poisonous', 'description': {'value': 'Der
# Fliegenpilz (Amanita muscaria), auch Roter Fliegenpilz genannt,  ist eine giftige Pilzart aus der Familie der
# Wulstlingsverwandten. Die Fruchtkörper erscheinen in Mitteleuropa von Juni bis zum Beginn des Winters,
# hauptsächlich von Juli bis Oktober.\nDie Giftwirkung des Fliegenpilzes wird wie bei verwandten Arten wie dem
# giftigeren Pantherpilz (Amanita pantherina) vor allem auf die toxische Wirkung der Ibotensäure sowie sekundär auf
# Muscarin zurückgeführt.Er wurde von der Deutschen Gesellschaft für Mykologie zum Pilz des Jahres 2022
# ernannt.\n\n', 'citation': 'https://de.wikipedia.org/wiki/Fliegenpilz', 'license_name': 'CC BY-SA 3.0',
# 'license_url': 'https://creativecommons.org/licenses/by-sa/3.0/'}, 'image': {'value':
# 'https://mushroom-id.ams3.cdn.digitaloceanspaces.com/knowledge_base/wikidata/2eb
# /2ebad87c493137cc89d68c6c3df3bb892e0a81d2.jpg', 'citation': '//commons.wikimedia.org/wiki/User:Onderwijsgek',
# 'license_name': 'CC BY-SA 3.0', 'license_url': 'https://creativecommons.org/licenses/by-sa/3.0/'}, 'language':
# 'de', 'entity_id': '509e11b658e98f03', 'name': 'Amanita muscaria'}
