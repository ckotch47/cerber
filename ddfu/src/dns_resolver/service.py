import dns.resolver
from print_color import print


class DnsResolverService:
    debug = False

    def resolve(self, domain: str = 'google.com', show_success: bool = True, show_failed: bool = False):
        res = dns.resolver.Resolver(configure=False)
        res.nameservers = ["8.8.8.8"]
        # Invoke try_ddr() to attempt to upgrade the connection via DDR
        res.try_ddr()
        # Do a sample resolution\
        try:
            for rr in res.resolve(domain, dns.rdatatype.A, search=True):
                if show_success or self.debug:
                    print(domain, rr.address, color='c', tag="success", tag_color='g')
                return rr.address
        except Exception as e:
            if show_failed or self.debug:
                print(domain, color='c', tag="fail", tag_color='r')
            return None
