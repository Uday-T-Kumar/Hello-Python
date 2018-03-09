import requests

r = requests.get('http://github.com')
print r.url
print r.status_code
print r.history

r = requests.get('http://github.com',allow_redirects=False)
print r.status_code
print r.history

r = requests.get('http://github.com',allow_redirects=True)
print r.status_code
print r.history

print requests.get('http://github.com',timeout=0.001)

