
from cerber.utils import ResponseCollector, FileBase, ProgressBarBase, RequestService, ResponseCollectorDto, Logger, \
    HeaderServices


class ScanApiList:
    file_path = None
    host = None
    show = []
    exclude = []
    progress_bar = ProgressBarBase(0, 'Find progress')

    result  = ResponseCollector

    def scan(self, host, file_path, show=None, exclude=None, header = None):
        if exclude is not None:
            self.exclude = exclude
        if show is not None:
            self.show = show

        file_base = FileBase(file_path)
        self.progress_bar.new_max(file_base.max)

        HeaderServices.set(header)

        for i in file_base.__iter__():
            if not i: break
            try:
                t = i.split(',')
                if t.__len__() == 2:
                    self.iteration(f"{host}/{t[1]}", t[0])
                else:
                    self.iteration(f"{host}/{i}")
            except Exception as e:
                Logger.error(e)

            self.progress_bar.__next__()

        self.progress_bar.__del__()

        ResponseCollector.print_response()



    def iteration(self, path: str, method='get'):
        res = RequestService.request(method, path)  # self._request(path)

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