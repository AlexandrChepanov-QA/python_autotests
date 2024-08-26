import requests
import pytest

URL = "https://api.pokemonbattle.ru/v2"
HEADER = {"Content-Type": "application/json"}
TOKEN = "c45ad8febb49e99086c73845b7fb3f4b"
TRAINER_ID = 4635

def test_status_code():
    response = requests.get(url=f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url=f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response_get.json()["data"][0]["id"] == "4635"