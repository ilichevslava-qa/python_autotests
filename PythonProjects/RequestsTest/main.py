import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '69783f56c4cd6fe76fb62a98898da47f'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
body_registration = {
    "trainer_token": TOKEN,
    "email": "iliva254@yandex.ru",
    "password": "Pivaiis254"
}
body_confirmation = {
    "trainer_token": TOKEN
    }
body_create = {
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}
body_change = {
    "pokemon_id": "generate",
    "name": "generate",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}
body_capture = {
    "pokemon_id": "28382"
}

'''responce = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(responce.text)'''

'''responce_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(responce_confirmation.text)'''

responce_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(responce_create.text)

message = responce_create.json()['message']
print(message)


responce_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(responce_change.text)

message = responce_change.json()['message']
print(message)


responce_capture = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_capture)
print(responce_capture.text)

message = responce_capture.json()['message']
print(message)