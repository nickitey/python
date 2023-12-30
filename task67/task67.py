# В этой задаче вам необходимо воспользоваться API сайта artsy.net
# API проекта Artsy предоставляет информацию о некоторых деятелях искусства, их работах, выставках.
# В рамках данной задачи вам понадобятся сведения о деятелях искусства (назовем их, условно, художники).
# Вам даны идентификаторы художников в базе Artsy.
# Для каждого идентификатора получите информацию об имени художника и годе рождения.
# Выведите имена художников в порядке неубывания года рождения. В случае если у художников одинаковый год рождения,
# выведите их имена в лексикографическом порядке.

import requests
import json
from operator import itemgetter


client_id = '35654c8bc6161674379b'
client_secret = 'dcd772c0ad9cd2eca63c63e0009ae066'

# инициируем запрос на получение токена
response = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                         data={
                             "client_id": client_id,
                             "client_secret": client_secret
                         })

# разбираем ответ сервера
response_json = json.loads(response.text)

# достаем токен
token = response_json["token"]
# eyJhbGciOiJIUzI1NiJ9.eyJyb2xlcyI6IiIsInN1YmplY3RfYXBwbGljYXRpb24iOiI3YWIxYjFjMS04ZWE3LTQ2NDktYjYxNy03NjliMDljZDhhYjQiLCJleHAiOjE3MDQ1NzcyMDAsImlhdCI6MTcwMzk3MjQwMCwiYXVkIjoiN2FiMWIxYzEtOGVhNy00NjQ5LWI2MTctNzY5YjA5Y2Q4YWI0IiwiaXNzIjoiR3Jhdml0eSIsImp0aSI6IjY1OTA4ZTMwZmYxZDg2MDAwZDA0ZjE2YiJ9.wCl3edvV03MprTT70RO3v09dMDKiwgKjLhbXRbEq9SM

# токен истекает
expires_at = response_json['expires_at']  # 2024-01-06T21:40:00+00:00


def get_artist_names(id):
    url = f'https://api.artsy.net/api/artists/{id}'
    headers = {
        'X-Xapp-Token': token
    }
    response = requests.get(url, headers=headers).json()
    return {'name': response['sortable_name'],
            'year': int(response['birthday'])
            }


artists = []
with open(r'dataset_24476_4.txt', 'r') as artist_codes:
    for string in artist_codes:
        artists.append(get_artist_names(string.strip()))

sorted_artists = sorted(artists, key=itemgetter('year', 'name'))


with open(r'result.txt', 'w', encoding='utf-8') as result:
    for artist in sorted_artists:
        result.write(artist['name'] + '\n')
