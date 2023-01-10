import json
import requests

j = {
    'name' : 'AsgharAgha',
    'ID' : 'Befarma97102225'
}

x = requests.post('https://www.toptal.com/developers/postbin/1673372629150-8168336732778', json = j)

print(x.status_code) # 200 ==> Successful

x = requests.get('https://www.toptal.com/developers/postbin/1673372629150-8168336732778')

print(x.text)
print(x.headers) 