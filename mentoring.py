import json
import requests

from Xenotyphlops.services.catfact import CatFact
from Xenotyphlops.utils.informator import Informator
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
cat = CatFact(url="https://catfact.ninja/fact")
print(f"zip.url: {zip._url}")
print(f"cat.url {cat._url}")
respz = zip.get_zipcode_info(zipcode="33162")
respc = cat.get_cat_fact_info()
print(respz)
print(respc)
informations = Informator
informations.get_informations(respz)
informations.get_informations(respc)
#Najebalem troche badziewia, zeby to sprawdzic jak nie moglem zasnac xDDD
# print(f"resp.status_code: {respz.status_code}")
# print(f"resp.status_code: {respc.status_code}")
# print(f"resp.headers: {respz.headers}")
# print(f"resp.headers: {respc.headers}")
# print(f"resp.text: {respz.json()}")
# print(f"resp.text: {respc.json()}")
print(respz.history)


text = json.loads(respz.text)
text_json = respz.json()

print(f"text_json['post code']: {text_json['post code']}")
