import requests

from Requests_Test.tests.test_pokemon import TRAINER_ID, URL

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '2b5f189fb7765eb6a388cdc9be96ad2e'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body_pok_creation = {
    "name": "TOTOSHKA",
    "photo_id": 7
}

responce_pok_creation = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_pok_creation)
print(responce_pok_creation.text)

pokemon_id = responce_pok_creation.json()['id']
print(pokemon_id)

body_pok_change = {
    "pokemon_id": pokemon_id,
    "name": "New Name",
    "photo_id": 2
}

responce_pok_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_pok_change)
print(responce_pok_change.text)

body_pok_add_pok = {
    "pokemon_id": pokemon_id,
}

responce_pok_add_pok = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pok_add_pok)
print(responce_pok_add_pok.text)


def part_of_responce():
    responce_get = requests.get(url = f'{URL}/trainers',params = {'trainer_id' : TRAINER_ID})
    assert responce_get.json()['name'] == 'Demonity'