import json
import logging
import requests

from typing import Dict, Any
from ...utils.requester import Requester
class UsersApi:

    def __init__(self, url):
        requester = Requester
        self._url = url
        url = "http://localhost:8080"

    # TODO zamienić poniższe requests na __requester
    def get_list_of_all_users(self, users: str) -> requests.Response:
        # self.requester(
        #     method="GET",
        #     url=f"{self._url}",
        #     headers={
        #         "accept": "application/xml"
        #     }
        # )
        return requests.get(url=f"{self._url}")

    def get_user_by_id(self, user_id: str) -> requests.Response:
        return requests.get(url=f"{self._url}/{user_id}")

    def create_user(self, user_data: dict) -> requests.Response:
        return requests.post(url=f"{self._url}", data=user_data)

    def update_user(self, user_id: str ,user_data: Dict[str, Any]) -> requests.Response:
        return requests.put(url=f"{self._url}/{user_id}", data=user_data)
