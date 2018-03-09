import requests

r = requests.get('http://httpbin.org/get')
print r.status_code

print (r.status_code == requests.codes.ok)

print r.headers
print r.headers['Content-Type']
print r.headers.get('content-type')

bad_r = requests.get('http://httpbin.org/status/404')
print bad_r.status_code
print r.raise_for_status()
print bad_r.raise_for_status()
