import requests


class CatFact:
    def __init__(self, url):
        self._url = url

    def get_cat_fact_info(self) -> requests.Response:
        return requests.get(url=f"{self._url}/")
