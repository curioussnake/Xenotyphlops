import requests


class Informator:

    def __init__(self, url):
        self._url = url

    def get_informations(self, resp: requests):
        print("response:" + str(resp))
        print(f"resp.status_code: {resp.status_code}")
        print(f"resp.headers: {resp.headers}")
        print(f"resp.text: {resp.json()}")
