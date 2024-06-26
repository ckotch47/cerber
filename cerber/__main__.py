from .src import arg_parser, SshCerber, PsqlCerber, HttpApiCerber, FtpCerber
import pyfiglet
from print_color import print


def main():
    print(
        pyfiglet.figlet_format('CERBER', font='larry3d'),
    )
    arg = arg_parser()
    if arg.m == 'ssh':
        SshCerber(arg.host, True).main(
            user=arg.u,
            passwd=arg.p,
            timeout=arg.t,
            bomb=arg.bomb,
            chunk=arg.w
        )
        return
    if arg.m == 'psql':
        db_name = arg.db if arg.db else 'postgres'
        PsqlCerber(host=arg.host, db_name=db_name, debug=True).main(
            user=arg.u,
            passwd=arg.p,
            timeout=arg.t,
            bomb=arg.bomb,
            chunk=arg.w
        )
        return
    if arg.m == 'http-get' or arg.m == 'http-post':
        method = str(arg.m).split('-')[1]
        HttpApiCerber(host=arg.host, method=method, header=arg.header, body=arg.body, debug=True).main(
            user=arg.u,
            passwd=arg.p,
            timeout=arg.t,
            bomb=arg.bomb,
            chunk=arg.w
        )
        return
    if arg.m == 'ftp':
        FtpCerber(arg.host, True).main(
            user=arg.u,
            passwd=arg.p,
            timeout=arg.t,
            bomb=arg.bomb,
            chunk=arg.w
        )
        return
