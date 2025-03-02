
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
        self.show = show.split(',') if show else []
        self.exclude = exclude.split(',') if exclude else []

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
        try:
            res = RequestService.get(path)
            if res is None:
                return
            if self.is_status_included(res.status_code):
                self.add_response(path, res.status_code, 'c', 'g')
            # else:
            #     self.add_response(path, res.status_code, 'c', 'r')
        except Exception as e:
            # Logger.error(f"Error during request to {path}: {e}")
            pass

    def is_status_included(self, status_code: int) -> bool:
        if self.show and str(status_code) in self.show:
            return True
        if self.exclude and str(status_code) in self.exclude:
            return False
        return 100 < status_code < 600

    def add_response(self, path: str, status_code: int, color: str, tag_color: str):
        ResponseCollector.response.append(
            ResponseCollectorDto(
                path, color, tag_color, str(status_code)
            )
        )