import json
import time
import uuid

import requests as req
from requests import Response

from ddfu.src.common.file_base import FileBase
from ddfu.src.common.progress_bar_base import ProgressBarBase
from print_color import print


class Fuzzing:
    url: str
    header: str
    method: str
    body: str
    res_data = []

    def __init__(self, url: str, method: str, header: str, body: str, worldlist: str, timeout: float):
        self.url = url
        self.method = method
        self.header = header if header else "{}"
        self.body = body if body else "{}"
        self.file = FileBase(worldlist)
        self.timeout = timeout
        self.debug = False
        self.bar = ProgressBarBase(name='fuzz', max_len=self.file.max)

    def fuzz(self):
        for elem in self.file.__iter__():
            if not self.debug:
                self.bar.__next__()

            url = self._replace_uuid(self.url)
            header = self._replace_uuid(self.header)
            body = self._replace_uuid(self.body)

            url = self._replace_fuzz(url, elem)
            header = self._replace_fuzz(header, elem)
            body = self._replace_fuzz(body, elem)

            res = self._request(url, header, body)
            self.res_data.append([url, res])
            if self.debug:
                self._print(url, res)
            time.sleep(self.timeout)

        if not self.debug:
            self.bar.__del__()
            for i in self.res_data:
                self._print(i[0], i[1])
        return

    def _request(self, url: str, header: str, body: str):
        return req.request(
            method=self.method.upper(),
            url=url,
            headers=json.loads(header),
            data=body
        )

    def _replace_uuid(self, value: str):
        return value.replace("FUZZUUID4", uuid.uuid4().__str__())

    def _replace_fuzz(self, name: str, value: str):
        return name.replace('FUZZ', value)

    def _print(self, url: str, res: Response):
        if res.status_code < 300:
            print(url, color='c', tag_color='g', tag=f"{res.status_code}")
        if 300 < res.status_code < 400:
            print(url, color='w', tag_color='y', tag=f"{res.status_code}")
        else:
            print(url, color='w', tag_color='r', tag=f"{res.status_code}")
