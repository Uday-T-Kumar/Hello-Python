import requests
import json

url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)
print(r.content)

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
print(r.text)

payload = (('key1', 'value1'),('key1','value2'))
r = requests.post("http://httpbin.org/post", data=payload)
print(r.text)

url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
r = requests.post(url, data=json.dumps(payload))
print (r.text)

r = requests.post(url, json=payload)
print(r.text)
