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

        if header is None:
            HeaderServices.set_default()
            header = HeaderServices.headers
        else:
            HeaderServices.set(json.dumps(header))

        try:
            time.sleep(RequestService.sleep_time)
            return httpx.get(
                url,
                headers=header,
                params=params,
                follow_redirects=RequestService.allow_redirects
            )
        except Exception as e:
            Logger.error(e)
            exit(1)