import json
import logging
import requests

from typing import Dict, Any
from utils.requester import Requester
class UsersApi:

    def __init__(self, url):
        self.requester = Requester()
        self._url = f"{url}/users"
        self.user_id = "1000"
        self.header = "application/json"
        self.firstname = "John"
        self.lastname = "Doe"
        self.role = "User"

    def set_headers(self, header) -> str:
        return f"accept: {header}" #Czy to na pewno tak?

    def get_list_of_all_users(self) -> requests.Response:
        return self.requester.requester(
            method="GET",
            url=f"{self._url}",
            headers=self.set_headers("application/xml")
        )

    def get_user_by_id(self, user_id: str) -> requests.Response:
        return self.requester.requester(
            method="GET",
            url=f"{self._url}/{self.user_id}",
            headers=self.set_headers("application/xml")
        )

    def create_user(self, firstname: str, lastname: str, role: str) -> requests.Response:
        return self.requester.requester(
            method="POST",
            url=f"{self._url}",
            headers=self.set_headers("application/xml"),
            data={#jak przekazywac body z data??
                "firstname": firstname,
                "lastname": lastname,
                "role": role
            }
        )

    def update_user(self, user_id: str ,user_data: Dict[str, Any]) -> requests.Response:
        return requests.put(url=f"{self._url}/{user_id}", data=user_data)

    def get_user_by_id_requests(self, user_id: str) -> requests.Response:
        return requests.get(url=f"{self._url}/{user_id}")

    def create_user_requests(self, user_data: dict) -> requests.Response:
        return requests.post(url=f"{self._url}", data=user_data)

    def update_user_requests(self, user_id: str ,user_data: Dict[str, Any]) -> requests.Response:
        return requests.put(url=f"{self._url}/{user_id}", data=user_data)

    # Jak przekazywac te dane do body do
