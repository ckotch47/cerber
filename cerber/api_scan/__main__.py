import pyfiglet

from cerber.api_scan.src.utils import arg_parser
from cerber.api_scan.src.openapi import OpenApi
from print_color import print


def main():
    print(
        pyfiglet.figlet_format('cerber - api'),
        color='c'
    )
    open_api = OpenApi(arg_parser(), success_only=False)
    open_api.openapi_scan_main()
