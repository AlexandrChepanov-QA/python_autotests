import requests

URL = "https://api.pokemonbattle.ru/v2"
HEADER = {"Content-Type": "application/json", "trainer_token": "c45ad8febb49e99086c73845b7fb3f4b"}
body_create = {
    "name": "Миддлсен", # боди для создания покемона
    "photo_id": 222 
}
body_knockout = {
    "pokemon_id": "45291" # боди покемона в нокаут
}
body_update = {
    "pokemon_id": "62518",
    "name": "Чейнт II", # боди для изменения покемона
    "photo_id": 158 
}
body_pokeball = {
    "pokemon_id": "62520" # боди для захвата покемона в покебол
} 



'''response_create = requests.post(f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)''' # запрос на создание покемона

'''response_knockout = requests.post(f'{URL}/pokemons/knockout', headers = HEADER, json = body_knockout)
print(response_knockout)''' # запрос на нокаут
'''message = response_knockout.json()['message']
print(message)''' # эта функция отвечает за поиск нужно ключа в json

'''response_update = requests.put(f'{URL}/pokemons', headers = HEADER, json = body_update)
print(response_update.text)''' # запрос на изменение покемона

'''response_pokeball = requests.post(f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_pokeball)
print(response_pokeball.text)''' # запрос на захват покемона в покебол 






