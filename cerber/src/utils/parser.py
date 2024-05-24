import argparse


def arg_parser():
    epilog_text = '''

    '''

    parser = argparse.ArgumentParser(
        description='Program for brutforce by port',
        epilog=epilog_text,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument(
        '--host',
        type=str,
        default=None,
        help='host for resolve'
    )

    parser.add_argument(
        '-u',
        type=str,
        default=None,
        help='user for login'
    )

    parser.add_argument(
        '-p',
        type=str,
        default=None,
        help='password for login'
    )

    parser.add_argument(
        '-header',
        type=str,
        default='{}',
        help='header for http json(string)'
    )

    parser.add_argument(
        '-body',
        type=str,
        default='{}',
        help='body for http json(string)'
    )

    parser.add_argument(
        '-m',
        type=str,
        default=None,
        help='method (ssh, ftp, http-get, http-post, psql, mysql)'
    )

    parser.add_argument(
        '-t',
        type=float,
        default=0.5,
        help='timeout for connection'
    )

    parser.add_argument(
        '-db',
        type=str,
        default=None,
        help='connect to databese (default psql = postgres)'
    )

    parser.add_argument(
        '-bomb',
        type=bool,
        default=False,
        required=False,
        action=argparse.BooleanOptionalAction,
        help='active cluster bomb for http-api'
    )

    parser.add_argument(
        '-w',
        type=float,
        default=2,
        help='cluster size'
    )



    return parser.parse_args()
