import time

import requests
from print_color import print
from ddfu.src.common.file_base import FileBase
from ddfu.src.common.progress_bar_base import ProgressBarBase


# class AdminFinder:
#     def __init__(self, filename):
#         self.wordlist = self.open(filename)
#         self.index = 0
#         self.max = len(self.wordlist)
#
#     def open(self, filename):
#         try:
#             with open(filename) as filehandle:
#                 return [line.strip('\n') for line in filehandle.readlines()]
#         except Exception as e:
#             print(e, color='red')
#             exit(1)
#
#     def __iter__(self):
#         self.index = 0
#         return self
#
#     def __len__(self):
#         return self.max
#
#     def __next__(self):
#         if self.index >= self.max:
#             raise StopIteration
#         else:
#             word = self.wordlist[self.index]
#             self.index += 1
#             return word

class AdminFinder:
    progress_bar = ProgressBarBase(0, 'Find progress')

    def __init__(self):
        self.exclude = None
        self.show = None
        self.res = []

    def _request(self, url, host):
        return requests.get(
            url=f'{url}'
        )

    def admin_finder_request(self, url: str, timeout: int = 0, filename: str = 'worldlist/admin-page.txt',
                             show: str = None, exclude: str = None):
        try:
            self.show = str(show).split(',') if show else None
            self.exclude = str(exclude).split(',') if exclude else None
        except:
            pass

        file_base = FileBase(filename)
        self.progress_bar.new_max(file_base.max)
        for i in file_base.__iter__():
            if not i:
                break
            res = self._request(f"{url}/{i}", url)
            if not self.show and 100 < res.status_code < 400:
                self.res.append({
                    "text": f"{url}/{i}",
                    "color": 'c',
                    "tag_color": 'g',
                    "tag": f'{res.status_code}'
                })
            elif self.show and str(res.status_code) in self.show:
                self.res.append({
                    "text": f"{url}/{i}",
                    "color": 'c',
                    "tag_color": 'g',
                    "tag": f'{res.status_code}'
                })

            if not self.exclude:
                pass
            elif self.exclude and not(100 < res.status_code < 400) and str(res.status_code) not in self.exclude:
                self.res.append({
                    "text": f"{url}/{i}",
                    "color": 'c',
                    "tag_color": 'r',
                    "tag": f'{res.status_code}'
                })

            self.progress_bar.__next__()
            time.sleep(timeout)

        self.progress_bar.__del__()
        self._print()

    def _print(self):
        for i in self.res:
            print(i['text'], color=i['color'], tag_color=i['tag_color'], tag=i['tag'])