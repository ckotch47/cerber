from cerber.ddfu.src import DnsBruteforceService, DnsResolverService, run_ddos_request, AdminFinder, dns_get_ptr, PortScan, Fuzzing
from print_color import print
import pyfiglet

from cerber.ddfu.utils.parser import m_arguments


def main_dns_resolve(arguments):
    dns_resolve = DnsResolverService()
    dns_bruteforce = DnsBruteforceService()
    dns_bruteforce.debug = False

    depth = 1 if arguments.r else 0

    if not arguments.host:
        return

    if not arguments.b:
        dns_resolve.resolve(arguments.host, show_failed=True)
    else:
        dns_bruteforce.bruteforce_domain(arguments.host, arguments.w, depth)
        dns_bruteforce.print_domains()
    return


def main():
    arguments = m_arguments
    print(
        pyfiglet.figlet_format("cerber"),
        color='c'
    )
    try:
        if arguments.ddos:
            run_ddos_request(arguments.host, arguments.port, arguments.t)
            return
        if arguments.admin:
            AdminFinder().admin_finder_request(arguments.host, arguments.timeout, arguments.w, arguments.so, arguments.exc)
            return
        if arguments.ip and not arguments.map:
            dns_get_ptr.get(arguments.ip)
            dns_get_ptr.print_()
            return
        if arguments.ip and arguments.map:
            PortScan().scan(arguments.ip, arguments.w)
            return
        if arguments.host and arguments.map:
            host_ip = DnsResolverService().resolve(arguments.host, show_failed=True)
            PortScan().scan(host_ip, arguments.w, arguments.tp)
            return
        if arguments.fuzz:
            Fuzzing(arguments.url, arguments.method,  arguments.header, arguments.body, arguments.w, arguments.timeout).fuzz()
            return
        main_dns_resolve(arguments)
    except KeyboardInterrupt:
        print('exit by user', color='r')
        return
    except Exception as e:
        print(e)
        return



