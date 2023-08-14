import json
import logging

import requests


class Requester:
    def requester(self, method, url, path="", body="", **kwargs):
        if "headers" in kwargs.keys() and "content-type" in kwargs["headers"].keys():
            data = json.dumps(body)
        else:
            data = body

        response = requests.request(
            method=method,
            url=f"{url}{'/' if path != '' else ''}{path}",
            data=data,
            headers=kwargs.get("headers", {})
        )
        logging.info(f"response.status_code: {response.status_code}")
        logging.info(f"response.headers: {response.headers}")
        logging.info(f"response.text: {response.text}")

        return response
