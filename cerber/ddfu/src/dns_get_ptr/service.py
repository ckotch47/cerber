import dns.resolver
from print_color import print


class DnsGetPtr:
    record = []

    def get(self, ip: str):
        print(ip)
        result = dns.resolver.resolve(f'{ip}.in-addr.arpa.', 'PTR')
        for val in result:
            self.record.append(val.to_text())
        return

    def print_(self):
        for i in self.record:
            print(i, color='c', tag='success', tag_color='g')


dns_get_ptr = DnsGetPtr()
