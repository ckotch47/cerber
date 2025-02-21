
from cerber.utils import Logger, FileBase, ProgressBarBase, ResponseCollector, ResponseCollectorDto, HeaderServices, \
    RequestService


class AdminFinder:
    progress_bar = ProgressBarBase(0, 'Find progress')
    exclude = []
    show = []

    def admin_finder_request(self,
                             url: str,
                             timeout: int = 0,
                             filename: str = 'worldlist/admin-page.txt',
                             show: str = None,
                             exclude: str = None):

        file_base = FileBase(filename)
        self.show = str(show).split(',') if show else []
        self.exclude = str(exclude).split(',') if exclude else []

        self.progress_bar.new_max(file_base.max)

        for i in file_base.__iter__():
            if not i: break
            try:
               self.iteration(f"{url}/{i}")
            except Exception as e:
                Logger.error(e)

            self.progress_bar.__next__()

        self.progress_bar.__del__()

        ResponseCollector.print_response()


    def iteration(self, path: str):
        res = RequestService.get(path) # self._request(path)
        if not self.show and 100 < res.status_code < 600 and str(res.status_code) not in self.exclude:
            ResponseCollector.response.append(
                ResponseCollectorDto(
                    path, 'c',
                    'g', f'{res.status_code}'
                )
            )

        elif self.show and str(res.status_code) in self.show:
            ResponseCollector.response.append(
                ResponseCollectorDto(
                    path, 'c',
                    'g', f'{res.status_code}'
                )
            )

        if not self.exclude:
            pass
        elif self.exclude and not (100 < res.status_code < 600) and str(res.status_code) not in self.exclude:
            ResponseCollector.response.append(
                ResponseCollectorDto(
                    path, 'c',
                    'r', f'{res.status_code}'
                )
            )
