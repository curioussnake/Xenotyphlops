import requests

from typing import Dict, Any
from utils.requester import Requester


class RolesApi:

    def __init__(self, url):
        self.requester = Requester()
        self._url = f"{url}/roles"

    def set_header(self, header) -> Dict[str, Any]:
        return {"accept": header}

    def get_list_of_all_roles(self) -> requests.Response:
        return self.requester.requester(
            method="GET",
            url=f"{self._url}",
            headers=self.set_header("application/xml")
        )
