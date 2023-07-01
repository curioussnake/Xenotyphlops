import json
import logging

import requests


class Requester:
    def requester(self, method, url, path="", body="", **kwargs):
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
        logging.info(f"resp.status_code: {response.status_code}")
        logging.info(f"resp.headers: {response.headers}")
        logging.info(f"resp.text: {response.text}")

        return response
