import requests

# Everything about your Pets

# Тип запроса GET
# Список проданных питомцев

status = 'sold'

res_get = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus?status={status}', headers={'accept': 'application/json'})

print(f'Статус кода: {res_get.status_code}')
print(res_get.text)
print(res_get.json())
print(type(res_get.json()))


# Тип запроса POST
# Добавить нового питомца

import requests

url = 'https://petstore.swagger.io/v2/pet'

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

data = {
    "id": 0,
    "category": {
        "id": 0,
        "name": "string"
    },
    "name": "doggie",
    "photoUrls": ["string"],
    "tags": [
        {
            "id": 0,
            "name": "string"
        }
    ],
    "status": "available"
}

res_post = requests.post(url, headers=headers, json=data)


print(f'Статус кода: {res_post.status_code}')
print(res_post.text)
print(res_post.json())
print(type(res_post.json()))

# Тип запроса DELETE
# Удалить питомца

res_delete = requests.delete(f'https://petstore.swagger.io/v2/pet/{9223372036854775807}', headers={'accept': 'application/json'})

print(f'Статус кода: {res_delete.status_code}')
print(res_delete.text)
print(res_delete.json())
print(type(res_delete.json()))


# Тип запроса PUT
# Изменение данных о питомце
url = 'https://petstore.swagger.io/v2/pet'

headers_put = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

data_put = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

res_put = requests.put(url, headers=headers_put, json=data_put)

print(f'Статус кода: {res_put.status_code}')
print(res_put.text)
print(res_put.json())
print(type(res_put.json()))
