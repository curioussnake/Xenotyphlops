import requests
from typing import Dict, Any, Union


class UsersApi:

    def __init__(self, url):
        self._url = url

    def get_list_of_all_users(self, users: str) -> requests.Response:
        return requests.get(url=f"{self._url}")

    def get_user_by_id(self, userId: str) -> requests.Response:
        return requests.get(url=f"{self._url}/{userId}")

    def create_user(self, userData: dict) -> requests.Response:
        return requests.post(url=f"{self._url}", data=userData)

    def update_user(self, userId: str ,userData: dict) -> requests.Response:
        return requests.put(url=f"{self._url}/{userId}", data=userData)