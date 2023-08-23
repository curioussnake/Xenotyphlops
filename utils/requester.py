import json
import logging

import requests


class Requester:
    def requester(self, method, url, path="", body="", **kwargs):
        headers = kwargs.get("headers", {})

        if "content-type" not in headers:
            headers["content-type"] = "application/json"

        if "application/json" == headers["content-type"]:
            data = json.dumps(body)
        else:
            data = body

        print(data)

        response = requests.request(
            method=method,
            url=f"{url}{'/' if path != '' else ''}{path}",
            data=data,
            headers=headers
        )
        logging.info(f"response.status_code: {response.status_code}")
        logging.info(f"response.headers: {response.headers}")
        logging.info(f"response.text: {response.text}")

        return response
