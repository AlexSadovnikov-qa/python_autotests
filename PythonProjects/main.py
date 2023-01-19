import requests
import json

token = '7fb9cf07ece24272c45163623c329c76'

# Запрос на регистрацию тренера
response_reg_trainer = requests.post('https://pokemonbattle.me:5000/trainers/reg', headers = {'Content-Type' : 'application/json', 
'trainer_token' : token},
json= {
"trainer_token": token,
    "email": "alex.sadov11@gmail.com",
    "password": "Sadko100993"
}
)
print(response_reg_trainer.text)

# Запрос на Активацию тренера (подтверждение почты)
response_confirm_email = requests.post('https://pokemonbattle.me:5000/trainers/confirm_email', headers = {'Content-Type' : 'application/json', 
'trainer_token' : token},
json= {
    "trainer_token": token
}
)
print(response_confirm_email.text)

# Запрос на создание покемона
response_new_pokemon = requests.post('https://pokemonbattle.me:5000/pokemons', headers = {'Content-Type' : 'application/json', 
'trainer_token' : token},
json = {
           "name": "Monster dragon",
   "photo": "https://www.pngmart.com/files/22/Pokemon-PNG-File.png"
})
print(response_new_pokemon.json()) 
pokemon_id = response_new_pokemon.json()['id']

# Запрос на изменение покемона
reponse_change = requests.put('https://pokemonbattle.me:5000/pokemons', headers = {'Content-Type' : 'application/json', 
'trainer_token' : token},
json = {
    "pokemon_id": pokemon_id, #менять данные покемона полученного выше или введите id покемона самостоятельно
    "name": "Big Dragon2",
    "photo": "https://www.freepnglogos.com/uploads/pokemon-png/pokemon-let-version-exclusive-pokemon-which-pokemon-38.png"
})
print(reponse_change.json())

# Запрос поймать покемона в покебол
response_add_pokeball = requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball', headers = {'Content-Type' : 'application/json', 
'trainer_token' : token},
json = {
         "pokemon_id": pokemon_id
})
print(response_add_pokeball.json())


