import json
import requests

stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
print(json.loads(stringOfJsonData))

url = 'http://httpbin.org/get'
response = requests.get(url)
response.raise_for_status()
data = json.loads(response.text)

print("headers:", data['headers'])
print("origin:", data["origin"])
print("url:", data["url"])




