import pyfiglet

from cerber.api_scan.src.list import ScanApiList
from cerber.api_scan.src.utils import arg_parser
from cerber.api_scan.src.openapi import OpenApi
from print_color import print


def main():
    print(
        pyfiglet.figlet_format('cerber - api'),
        color='c'
    )
    m_arg = arg_parser()
    if m_arg.l is None:
        open_api = OpenApi(m_arg, success_only=False)
        open_api.openapi_scan_main()
    else:
        scan_api_list = ScanApiList()
        scan_api_list.scan(m_arg.host, m_arg.w, m_arg.so, m_arg.exc, m_arg.header)
