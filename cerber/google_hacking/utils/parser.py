import argparse

epilog_text = '''
        cerberus-gh --host google.com -m 1                                                : for find ip and dns recon
        
        available methods for m
        1 - Publicly exposed documents
        2 - Directory listing vulnerabilities
        3 - Configuration files exposed
        4 - Database files exposed
        5 - Log files exposed
        6 - Backup and old files
        7 - Login pages
        8 - SQL errors
        9 - PHP errors / warning
        10 - phpinfo()
        11 - Search pastebin.com / pasting sites
        12 - Search github.com and gitlab.com
        13 - Search stackoverflow.com
        14 - Signup pages
        15 - Find Subdomains
        16 - Find Sub-Subdomains
        17 - Search in Wayback Machine
'''

parser = argparse.ArgumentParser(
    description='Program for simple google hacking',
    epilog=epilog_text,
    formatter_class=argparse.RawDescriptionHelpFormatter)

parser.add_argument(
    '--host',
    type=str,
    default=None,
    help='host for resolve'
)

parser.add_argument(
    '-m',
    type=int,
    default=1,
    required=False,
    help='Method for scan'
)
parser.add_argument(
    '-l',
    type=bool,
    default=False,
    required=False,
    action=argparse.BooleanOptionalAction,
    help='print list for self search'
)
m_arguments = parser.parse_args()
