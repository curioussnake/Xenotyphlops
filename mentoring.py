import json
import requests

from services.catfact import CatFact
from utils.informator import Informator
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

print(respz.history)


text = json.loads(respz.text)
text_json = respz.json()

print(f"text_json['post code']: {text_json['post code']}")
