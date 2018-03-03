import requests
import json

#r = requests.get('https://gist.githubusercontent.com/Uday-T-Kumar/d31bf7bc3ec04b1fdbc22ae86bf769c7/raw/9fe56838f7d670dec5620bfd3fb5b7261e844685/sample_gist.json')
#r = requests.get('https://gist.githubusercontent.com/Uday-T-Kumar/d31bf7bc3ec04b1fdbc22ae86bf769c7/raw/803d713357bda4d9e5d157345347ba3cd143c44d/sample_gist.json')
r = requests.get('https://gist.github.com/Uday-T-Kumar/d31bf7bc3ec04b1fdbc22ae86bf769c7')
print r.content

data = r.content
data_dict = json.loads(data)
print data_dict

print len(data_dict)
