import logging

import requests


class Informator:

    def __init__(self, url):
        self._url = url

    def get_informations(self, resp: requests):
        logging.info("response:" + str(resp))
        logging.info(f"resp.status_code: {resp.status_code}")
        logging.info(f"resp.headers: {resp.headers}")
        logging.info(f"resp.text: {resp.json()}")

