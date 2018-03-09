import requests

r = requests.get('https://api.github.com/events')
print ('GET- Content:'+ r.content) 
print (r.status_code)

r = requests.post('http://httpbin.org/post', data = {'key':'value'})
print ('POST- Content:'+ r.content)
print (r.status_code)

r = requests.put('http://httpbin.org/put', data = {'key':'value'})
print ('PUT- Content:'+ r.content)
print (r.status_code)

r = requests.delete('http://httpbin.org/delete')
print ('DELET- Content:'+ r.content)
print (r.status_code)

r = requests.head('http://httpbin.org/get')
print ('HEAD- Content:'+ r.content)
print (r.status_code)

r = requests.options('http://httpbin.org/get')
print ('OPTIONS- Content:'+ r.content)
print (r.status_code)
