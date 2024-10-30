import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '2b5f189fb7765eb6a388cdc9be96ad2e'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = 7793

def test_status_code():
    responce = requests.get(url = f'{URL}/trainers',params = {'trainer_id' : TRAINER_ID})
    assert responce.status_code == 200

def test_part_of_responce():
    responce_get = requests.get(url = f'{URL}/trainers',params = {'trainer_id' : TRAINER_ID})
    assert responce_get.json()["data"][0]["trainer_name"] == 'Demonity'



    

