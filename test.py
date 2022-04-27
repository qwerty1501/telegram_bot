import requests
import json
r = requests.get('https://api.tez-shop.com.kg/prod-list/?format=json')
data = r.json()
print(data[-1]['name'])