import requests
from typing import Dict, Any, Union


class ZipCode:

    def __init__(self, url):
        self._url = url

    def get_zipcode_info(self, zipcode: str) -> requests.Response:
        return requests.get(url=f"{self._url}/{zipcode}")
