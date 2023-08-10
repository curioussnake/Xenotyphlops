import requests

from typing import Dict, Any
from utils.requester import Requester
from utils.validation import Validation


class RolesApi:

    def __init__(self, url):
        self.requester = Requester()
        self._url = f"{url}/roles"
        self.validation = Validation()

    def get_list_of_all_roles(self) -> requests.Response:
        return self.requester.requester(
            method="GET",
            url=f"{self._url}",
            headers=self.validation.set_header("application/xml")
        )
