import argparse


def arg_parser():
    epilog_text = '''
Program for dns resolve and ddos server by url
Example usage: 
    cerber-api --host [:1] -w openapi.json -header header.json -show 200,201 
    cerber-api --host [:1] -w openapi.json -header header.json -exclude 401,401
    cerber-ap --host [:1] -w openapi.json -header header.json 
    '''

    parser = argparse.ArgumentParser(
        description=epilog_text,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument(
        '--host',
        type=str,
        default=None,
        help='host for resolve'
    )

    parser.add_argument(
        '-w',
        type=str,
        default=None,
        help='path to file openapi.json'
    )

    parser.add_argument(
        '-header',
        type=str,
        default=None,
        help='path to file headers.json'
    )
    # dispatcher
    parser.add_argument(
        '-s',
        type=bool,
        default=False,
        required=False,
        action=argparse.BooleanOptionalAction,
        help='show success only (dispatcher)'
    )
    parser.add_argument(
        '-so',
        type=str,
        default=None,
        help='show only (example -show 200,201)'
    )
    parser.add_argument(
        '-exc',
        type=str,
        default=None,
        help='show only (example -exclude 401, 403)'
    )

    return parser.parse_args()
