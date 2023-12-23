import json
import logging
import requests

from typing import Dict, Any
from utils.requester import Requester
from utils.validation import Validation


class UsersApi:

    def __init__(self, url):
        self.requester = Requester()
        self._url = f"{url}/users"
        self.validation = Validation()

    def get_list_of_all_users(self, accept: str = "application/json") -> requests.Response:
        return self.requester.requester(
            method="GET",
            url=f"{self._url}",
            headers=self.validation.set_header(accept)
        )

    def get_user_by_id(self, user_id: str, accept: str = "application/xml") -> requests.Response:
        return self.requester.requester(
            method="GET",
            url=f"{self._url}/{user_id}",
            headers=self.validation.set_header(accept)
        )

    def create_user(self, name: str, lastname: str, accept: str = "application/json", **kwargs) -> requests.Response:  # Jezeli jest none to znaczy, ze wartosc jest opcjonalna
        body = {
            "name": name,
            "lastname": lastname,
        }
        if "role" in kwargs.keys():
            body.update({"role": kwargs["role"]})

            # jezeli wartosc role jest opcjonalna i nie chcemy jej definiowac jako role: str = None, to mozna wykorzystac
            # kwargs jak w definicji powyzej. Z wykorzystaniem metody update na slowniku body.

        return self.requester.requester(
            method="POST",
            url=f"{self._url}",
            headers=self.validation.set_header(accept),
            body=body
        )

    def update_user(self, user_id: str, name: str, lastname: str, role: str, accept: str = "application/json") -> requests.Response:
        return self.requester.requester(
            method="PUT",
            url=f"{self._url}/{user_id}",
            headers=self.validation.set_header(accept),
            body={
                "name": name,
                "lastname": lastname,
                "role": role
            }
        )

    def delete_user(self, user_id: str, accept: str = "appliation/json") -> requests.Response:
        return self.requester.requester(
            method="DELETE",
            url=f"{self._url}/{user_id}",
            headers=self.validation.set_header(accept),
        )

