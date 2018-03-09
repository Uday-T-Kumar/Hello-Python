import requests

url = 'https://httpbin.org/cookies'
cookies  = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)

print r.status_code
print r.text

jar = requests.cookies.RequestsCookieJar()
jar.set('tasty_cookie','yum',domain='httpbin.org',path='/cookies')
jar.set('gross_cookies','blech',domain='httpbin.org',path='/elsewhere')

r = requests.get(url, cookies=jar)
print r.text
