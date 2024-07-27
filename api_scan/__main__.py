import pyfiglet

from api_scan.src.utils import arg_parser
from api_scan.src.openapi import OpenApi
from print_color import print


def main():
    print(
        pyfiglet.figlet_format('cerber api', font='larry3d',),
        color='c'
    )
    open_api = OpenApi(arg_parser(), success_only=False)
    open_api.openapi_scan_main()
