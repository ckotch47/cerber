import os

from cerber.ddfu.src.dns_resolver.service import DnsResolverService
from print_color import print
from cerber.ddfu.src.common.progress_bar_base import ProgressBarBase


class DnsBruteforceService(DnsResolverService):
    path = 'worldlist'
    domains = []
    scanned_domain = []
    file_len = 0
    progress_bar = ProgressBarBase(0, 'Scan progress')

    def _get_file(self, path: str = None, size: int = None) -> list[str]:
        file_path = self._get_file_path(path, size)
        if not os.path.exists(file_path):
            print(f"File {file_path} not found")
            exit(-1)
        try:
            with open(file_path) as file:
                return [line.strip() for line in file.readlines()]
        except Exception as e:
            print(f"Error reading file: {e}")
            exit(-1)

    def _get_file_path(self, path: str = None, size: int = 100) -> str:
        if path is None:
            if size in {100, 500, 1000, 10000}:
                return f'{self.path}/subdomains-{size}.txt'
        return path if path else None

    def _resolve_subdomain(self, subdomain: str):
        if subdomain not in self.scanned_domain:
            r = self.resolve(subdomain, False)
            if r:
                self.scanned_domain.append(subdomain)
                self.domains.append([subdomain, r])

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

        for i in sub_list:
            self._resolve_subdomain(f'{i}.{domain}')
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
