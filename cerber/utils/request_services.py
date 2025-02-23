import json
import time

import httpx
from cerber.utils import HeaderServices, Logger

class RequestService:
    timeout = 30
    allow_redirects = False
    sleep_time = 0.1

    @staticmethod
    def get(url: str, params=None, header=None):
        if params is None:
            params = {}

        try:

            time.sleep(RequestService.sleep_time)
            return httpx.get(
                url,
                headers=header if header else HeaderServices.headers,
                params=params,
                follow_redirects=RequestService.allow_redirects
            )
        except Exception as e:
            Logger.error(e)
            return None

    @staticmethod
    def request(method, url: str, payload=None, header=None):
        if payload is None:
            payload = {}

        try:

            time.sleep(RequestService.sleep_time)
            return httpx.request(
                method,
                url,
                headers=header if header else HeaderServices.headers,
                params=payload,
                data=payload,
                follow_redirects=RequestService.allow_redirects
            )
        except Exception as e:
            Logger.error(e)
            exit(1)