import dns.resolver
from print_color import print

from cerber.utils import Logger, ResponseCollector


class DnsResolverService:
    debug = False



    def resolve(self, domain: str = 'google.com', show_success: bool = True, show_failed: bool = False):
        res = dns.resolver.Resolver(configure=False)
        res.nameservers = ["8.8.8.8"]

        res.try_ddr()

        try:
            for rr in res.resolve(domain, dns.rdatatype.A, search=True):
                if show_success or self.debug:
                    ResponseCollector.print_success(f"{domain} -> {rr.address}")
                return rr.address
        except Exception as e:
            return None
