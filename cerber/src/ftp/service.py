from cerber.src.utils.service_base import CerberBase
from ftplib import FTP
from print_color import print


class FtpCerber(CerberBase):
    def connect(self, user: str, passwd: str, timeout: float):

        try:
            ftp = FTP(self.host, timeout=timeout)
            ftp.port = self.port
            ftp.login(user, passwd)

            data = ftp.nlst()
            print(f"{user}:{passwd}", tag='success', tag_color='green')
            return data
        except Exception as e:
            if self.debug:
                print(f"{user}:{passwd}", tag='fail', tag_color='red')
            return None
