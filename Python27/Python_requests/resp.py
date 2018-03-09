import requests

r = requests.get('https://api.github.com/events')
print r.text
print r.encoding

r.encoding = 'ISO-8859-1'
print r.encoding
print r.text

print r.json

print r.raw
print r.raw.read(10)

with open('/home/eudayku/Python_requests/output.txt', 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)
