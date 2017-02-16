import requests
r=requests.get('http://google.com')
print(r)
print(r.status_code)
print(r.encoding)
#print(r.text)
