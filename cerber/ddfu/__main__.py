from importlib import metadata

from cerber.ddfu.src import DnsBruteforceService, DnsResolverService, run_ddos_request, AdminFinder, dns_get_ptr, PortScan, Fuzzing, OSDetector
from cerber.utils import Logger, RequestService
from print_color import print
import pyfiglet

from cerber.ddfu.utils.parser import m_arguments

Logger.log_level = 0

def main_dns_resolve(arguments):
    try:
        arguments.host = arguments.host.replace('http://', '').replace('https://', '')
    except:
        pass
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

    return


def main():
    arguments = m_arguments

    print(
        pyfiglet.figlet_format("cerber"),
        color='c'
    )
    try:
        if arguments.timeout:
            RequestService.sleep_time = int(arguments.timeout)

        if arguments.v:
            print(metadata.version('cerber'))
            return

        if arguments.ddos:
            run_ddos_request(arguments.host, arguments.port, arguments.t)
            return
        if arguments.admin:
            AdminFinder().admin_finder_request(arguments.host, arguments.timeout, arguments.w, arguments.so, arguments.exc)
            return

        if arguments.ip:
            if arguments.os:
                detector = OSDetector()
                detector.run(arguments.ip)
                return
            elif arguments.map:
                PortScan().scan(arguments.ip, arguments.w)
            else:
                dns_get_ptr.get(arguments.ip)
                dns_get_ptr.print_()


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



