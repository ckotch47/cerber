from ddfu.src.dns_resolver.service import DnsResolverService
from print_color import print
from ddfu.src.common.progress_bar_base import ProgressBarBase


class DnsBruteforceService(DnsResolverService):
    path = 'worldlist'
    domains = []
    scanned_domain = []
    file_len = 0
    progress_bar = ProgressBarBase(0, 'Scan progress')

    def _get_file(self, path: str = None, size: int = None):
        try:
            file_path = self._get_file_path(path, size)
            file = open(file_path)
            res = []
            for i in file.readlines():
                res.append(i.splitlines()[0])
            return res
        except Exception as e:
            print('None file', tag_color='red', tag='failed')
            exit(-1)

    def _get_file_path(self, path: str = None, size: int = 100):
        file_path = None
        if path is None:
            if size == 100 or \
                    size == 500 or \
                    size == 1000 or \
                    size == 10000:
                file_path = f'{self.path}/subdomains-{size}.txt'
        elif path:
            file_path = path

        return file_path

    def bruteforce_domain(self,
                          domain: str = None,
                          path: str = None,
                          depth: int = 0,
                          size: int = None):

        if domain not in self.scanned_domain:
            self.scanned_domain.append(domain)
            self.domains.append([f'{domain}', self.resolve(domain, False)])

        sub_list = self._get_file(path, size)
        self.file_len = self.file_len + len(sub_list)

        self.progress_bar.new_max(self.file_len)
        # progres_bar = IncrementalBar('Scan progress', max=len(sub_list), color='cyan')

        for i in sub_list:
            if f'{i}.{domain}' not in self.scanned_domain:
                r = self.resolve(f'{i}.{domain}', False)
                if r:
                    self.scanned_domain.append(f'{i}.{domain}')
                    self.domains.append([f'{i}.{domain}', r])
            if not self.debug:
                self.progress_bar.__next__()

        if depth == 0:
            return

        for domain in self.domains:
            self.bruteforce_domain(domain[0], path, depth - 1, size)

        self.progress_bar.__del__()
        return

    def print_domains(self):
        for i in self.domains:
            print(f'{i[0]}  {i[1]}', tag_color='g', tag='success', color='c')
