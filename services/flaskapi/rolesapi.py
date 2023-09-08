import requests

from typing import Dict, Any
from utils.requester import Requester
from utils.validation import Validation


class RolesApi:

    def __init__(self, url):
        self.requester = Requester()
        self._url = f"{url}/roles"
        self.validation = Validation()

    def get_list_of_all_roles(self, accept: str = "application/json") -> requests.Response:
        return self.requester.requester(
            method="GET",
            url=f"{self._url}",
            headers=self.validation.set_header(accept)
        )

    def get_role_by_id(self, role_id: str, accept: str = "application/json") -> requests.Response:
        return self.requester.requester(
            method="GET",
            url=f"{self._url}/{role_id}",
            headers=self.validation.set_header(accept)
        )
