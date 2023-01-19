import requests
import pytest

# Проверка статус кода ответа 200
def test_status_code():
    response = requests.get('https://pokemonbattle.me:5000//trainers')
    assert response.status_code == 200


# Получение информации по тренеру
def test_trainer_info():
    response = requests.get('https://pokemonbattle.me:5000//trainers', params = {'trainer_id' : '1817'})
    assert response.json()['trainer_name'] == 'SADKO'



