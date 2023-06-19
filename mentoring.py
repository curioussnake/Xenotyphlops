import json
import requests
from services.zipcode import ZipCode


# resp = requests.get("http://localhost")

# body = {
#     "id": 1001,
#     "name": "geek",
#     "passion": "coding",
# }
#
# content_len = len(body)
# https://api.zippopotam.us/us/33162
zip = ZipCode(url="https://api.zippopotam.us/us")
print(f"zip.url: {zip._url}")
resp = zip.get_zipcode_info(zipcode="33162")
print(resp)
print(f"resp.status_code: {resp.status_code}")
print(f"resp.headers: {resp.headers}")
print(f"resp.text: {resp.json()}")

text = json.loads(resp.text)
text_json = resp.json()

print(f"text_json['post code']: {text_json['post code']}")
