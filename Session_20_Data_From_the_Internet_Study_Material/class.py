'''
Api - application program interface
https:// api.example.com

https - hypter text transser protocl secure
api.example.com - server
/products - endpoint

https://drive.google.com/drive/folders/1JhdYQqLEnRMoBir54biWE9Jtac7S092X

protocol - https
server - drive.google.com
endpoint - drive/fodlers/....

'''

import requests

response = requests.get(
    "https://dummyjson.com/products"
)
parameters={
    'username': 'prabhanjan',
    'password': 12345
}
response = requests.get(url='https://dummyjson.com/products',params = parameters)
# print(response.status_code)
'''
token = 12345
'''
# response = requests.get(url='https://dummyjson.com/products',params = token)
# print(response.text)

data = response.json()
print(data)
products = data["products"]
print(product[0]['title'])
print(product[0]['price'])
print(product[0]['dimensions']['width'])
print(product[0]['tags'][0])

for product in products:
    # print(product['title'], product['price'], product['dimensions']['width'], product['tags'][0])
    if product['price']>500:
        print(product['title'])


'''
api which have authentication 
params(parametes)
https://dummyjson.com/username=prabhanjan&password=1234[set_of_permissoions] read the products data
token - 1234567890(certain amount of time) 15mins
https://dummyjson.com/products/token=1234567890 
'''