import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '69783f56c4cd6fe76fb62a98898da47f'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
TRENER_ID = '2634'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trener_id' : TRENER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trener_id' : TRENER_ID})
    assert response_get.json()["data"][0]["name"] == 'Бульбазавр'


@pytest.mark.parametrize('key, value', [('name', 'Бульбазавр'), ('trainer_id', TRENER_ID), ('pokemon_id', '28382')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trener_id' : TRENER_ID})
    assert response_parametrize.json()["data"][0][key] == value
    