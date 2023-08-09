import json
import logging
import requests

from typing import Dict, Any
from utils.requester import Requester


class UsersApi:

    def __init__(self, url):
        self.requester = Requester()
        self._url = f"{url}/users"

    # TODO do set_header header ma byc headers i zawierac naglowki ktore chcesz
    #      zaaktualizowac a w metodzie naglowki maja byc zdefiniowane z defaultowymi wartosciami.
    #      Jezeli zostanie przekazany naglowek ktory nie jest zdefiniowany wsrod naglowkow, ma zostac dodany.
    def set_header(self, header) -> Dict[str, Any]:
        return {"accept": header}

    def get_list_of_all_users(self) -> requests.Response:
        return self.requester.requester(
            method="GET",
            url=f"{self._url}",
            headers=self.set_header("application/xml")
        )

    def get_user_by_id(self, user_id: str) -> requests.Response:
        return self.requester.requester(
            method="GET",
            url=f"{self._url}/{user_id}",
            headers=self.set_header("application/xml")
        )

    def create_user(self, name: str, lastname: str, **kwargs) -> requests.Response:  # Jezeli jest none to znaczy, ze wartosc jest opcjonalna
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
            headers=self.set_header("application/xml"),
            data=body
        )

    def update_user(self, user_id: str, name: str, lastname: str, role: str) -> requests.Response:
        return self.requester.requester(
            method="PUT",
            url=f"{self._url}/{user_id}",
            headers=self.set_header("application/xml"),
            data={
                "name": name,
                "lastname": lastname,
                "role": role
            }
        )
