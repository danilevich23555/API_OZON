import requests
import os
import datetime



ApiKey=''
ClientId=''
HEADERS =  {
        'Api-Key': ApiKey,
        'Client-Id': ClientId,
        'Content-type': 'application/json'
    }


url = 'https://api-seller.ozon.ru/v1/actions'
response = requests.get(url=url, headers=HEADERS)
temp=[]
print(response.json()['result'])
[temp.append({'id': x['id'], 'title': x['title'], 'date_start': x['date_start'],
              'date_end': x['date_end']}) for x in response.json()['result']]


HEADERS =  {
        'Api-Key': ApiKey,
        'Client-Id': ClientId,
        'Content-type': 'application/json'
    }
for x in response.json()['result']:
    print(f"Эта акция {x['title']} проходит с {x['date_start']} по {x['date_end']}, в ней участвоют следующие товары:")
    json  = {"action_id": x['id'], "limit": 0, "offset": 0}
    url = 'https://api-seller.ozon.ru/v1/actions/candidates'
    response2 = requests.post(url=url, headers=HEADERS, json=json)
    temp=[]
    for y in response2.json()['result']['products']:
        HEADERS =  {
                'Api-Key': ApiKey,
                'Client-Id': ClientId,
                'Content-type': 'application/json'
            }

        json  = {"product_id": y['id']}
        url = 'https://api-seller.ozon.ru/v1/product/info/description'
        response3 = requests.post(url=url, headers=HEADERS, json=json)
        print(f' {response3.json()["result"]["name"]}, цена без акции состовляет {y["price"]}, по акции можно приобрести с ценой '
              f'{y["max_action_price"]}')