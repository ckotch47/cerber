import dns.resolver
from print_color import print

from cerber.utils import Logger


class DnsResolverService:
    debug = False

    @staticmethod
    def _print_success(domain: str, address: str):

        print(f"{domain} -> {address}", color='c', tag="success", tag_color='g')

    @staticmethod
    def _print_failure(domain: str):
        print(domain, color='c', tag="fail", tag_color='r')

    def resolve(self, domain: str = 'google.com', show_success: bool = True, show_failed: bool = False):
        """
        Resolves the IP address of the given domain.

        :param domain: The domain to resolve.
        :param show_success: Whether to print successful resolutions.
        :param show_failed: Whether to print failed resolutions.
        :return: The resolved IP address or None if resolution fails.
        """
        res = dns.resolver.Resolver(configure=False)
        res.nameservers = ["8.8.8.8"]

        res.try_ddr()

        try:
            for rr in res.resolve(domain, dns.rdatatype.A, search=True):
                if show_success or self.debug:
                    self._print_success(domain, rr.address)
                return rr.address
        except Exception as e:
            Logger.error(e)
            exit(1)
