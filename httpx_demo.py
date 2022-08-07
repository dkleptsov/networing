import httpx
import requests

r = httpx.get('https://www.example.org/')
# r = requests.get('https://www.google.org/')
print(r)
print(r.status_code)
print(r.headers['content-type'])
print(r.text)