import json

from cerber.src.utils import CerberBase
from print_color import print
import timeit
import httpx


class HttpApiCerber(CerberBase):
    def __init__(self, host: str, method: str, header: str, body: str, debug=False):
        if method == 'get' or method == 'post':

            self.method = method
            self.header = header
            self.body = body
            super().__init__(host, debug)
        else:
            self.raise_err(f"Method - {method} not found", -101)

    def connect(self, user: str, passwd: str, timeout: float):
        if self.port:
            url = f"{self.host}:{self.port}"
        else:
            url = f"{self.host}"
        header = self.header
        body = self.body

        url = self._replace(url, user, passwd)
        header = self._replace(header, user, passwd)
        body = self._replace(body, user, passwd)
        start = 0
        stop = 0
        try:
            # print(url, self.method, header, body)
            start = timeit.default_timer()
            tmp = self._request(url, self.method, header, body)
            stop = timeit.default_timer()
            tmp.raise_for_status()

            print(f"[Time request]: {round((stop - start), 3)} | {user}:{passwd}", tag='success', tag_color='green')
            return [round((stop - start), 3), user, passwd, 'success']
        except Exception as e:
            if self.debug:
                print(f"[Time request]: {round((stop - start), 3)} | {user}:{passwd} | {str(e).split('\n')[0]}", tag='fail', tag_color='red')
            return None

    def _request(self, url: str, method: str, header: str, body: str):
        if method == 'get':
            return httpx.get(url=url, headers=json.loads(header), params=json.loads(body))
        elif method == 'post':
            return httpx.post(url=url, headers=json.loads(header), json=json.loads(body))

    @staticmethod
    def _replace(val: str, *args):
        try:
            for j in range(len(args)):
                val = val.replace(f'${j + 1}$', args[j])
            return val
        except:
            return val


    @staticmethod
    def _header_to(header: dict) -> list[tuple[str, str]]:
        res = []
        for i in header.keys():
            res.append((i, header[i]))

        return res
