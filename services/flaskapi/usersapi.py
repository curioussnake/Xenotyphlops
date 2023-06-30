import json

import requests
from typing import Dict, Any


class UsersApi:

    def __init__(self, url):
        # TODO IDEA url="http://localhost:8080 a poniżej powinno się dodać /users
        self._url = url

    # TODO przenieść do util żeby był reużywalny między różnymi modułami
    def __requester(self, method, url, path="", body="", **kwargs):
        if "headers" in kwargs.keys() and "content-type" in kwargs["headers"].keys():
            data = json.dumps(body)
        else:
            data = body
        # TODO dodać aktualicacje headers i ich przekazanie do request (jak aktualizować wartości w słowniku?)
        response = requests.request(
            method=method,
            url=f"{url}{'/' if path != '' else ''}{path}",  # TODO do przemyślenia czy nie można prościej
            data=data
        )
        # TODO zamień print na logger
        print(f"resp.status_code: {response.status_code}")
        print(f"resp.headers: {response.headers}")
        print(f"resp.text: {response.text}")
        return response

    # TODO zamienić poniższe requests na __requester
    def get_list_of_all_users(self, users: str) -> requests.Response:
        self.__requester(
            method="GET",
            url=f"{self._url}",
            headers={
                "accept": "application/xml"
            }
        )
        return requests.get(url=f"{self._url}")

    def get_user_by_id(self, user_id: str) -> requests.Response:
        return requests.get(url=f"{self._url}/{user_id}")

    # TODO pozmieniać nazwy zmienny na snake case
    def create_user(self, userData: dict) -> requests.Response:
        return requests.post(url=f"{self._url}", data=userData)

    def update_user(self, userId: str ,userData: Dict[str, Any]) -> requests.Response:
        return requests.put(url=f"{self._url}/{userId}", data=userData)
