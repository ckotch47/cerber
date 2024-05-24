import math
import threading

from .file_base import FileBase
from print_color import print


class CerberBase:
    debug = False

    def __init__(self, host: str, debug=False):
        self.debug = debug
        try:
            tmp = host.split(':')
            if len(tmp) > 2:
                self.host = host.replace(f":{tmp[-1]}", '')
                self.port = tmp[-1]
            else:
                self.host = host
                self.port = None
        except:
            self.host = host
            self.port = 22

    def connect(self, user: str, passwd: str, timeout: float):
        pass

    def main(self, user: str, passwd: str, timeout: float, bomb: bool = False, chunk: int = 4):
        if bomb:
            return self.main_bomb(user, passwd, timeout, chunk)
        tmp_user, tmp_passwd = self._get_user_passwd(user, passwd)
        return self.brute_force(tmp_user, tmp_passwd, timeout)

    def main_bomb(self, user: str, passwd: str, timeout: float, chunk: int = 4):
        tmp_user, tmp_passwd = self._get_user_passwd(user, passwd)
        thm_chunk = math.ceil(tmp_user.max/chunk)
        if isinstance(tmp_user, FileBase) and isinstance(tmp_passwd, FileBase):
            tmp_user_chunk = self.get_chunks(tmp_user.__getfile__(), thm_chunk)
            for i in range(math.ceil(len(tmp_user) / thm_chunk)):
                threading.Thread(target=self.brute_force_bomb, args=(tmp_user_chunk.__next__(), tmp_passwd.__getfile__(), timeout)).start()

    def brute_force(self, user: str | FileBase, passwd: str | FileBase, timeout: float):
        if (not isinstance(user, FileBase)  # if user and password str
                and not isinstance(passwd, FileBase)):
            self.connect(user, passwd, timeout)
            return

        if isinstance(user, FileBase):  # if user is File
            for user_i in user.__iter__():  # run cycle
                if isinstance(passwd, FileBase):  # if password is File
                    for passwd_i in passwd.__iter__():  # run cycle for password
                        if self.connect(user_i, passwd_i, timeout):  # connect user_iteration password_iteration
                            return
                else:  # if password not file
                    if self.connect(user_i, passwd, timeout):  # conn user_iteration password
                        return
        else:  # if user not file
            if isinstance(passwd, FileBase):  # if password is file
                for passwd_i in passwd.__iter__():  # run cycle
                    if self.connect(user, passwd_i, timeout):  # connect user and password_iteration
                        return
            else:  # else
                if self.connect(user, passwd, timeout):  # else connect user password
                    return

    def brute_force_bomb(self, user: str | tuple, passwd: str | list, timeout: float):
        if (not isinstance(user, tuple)  # if user and password str
                and not isinstance(passwd, tuple)):
            self.connect(user, passwd, timeout)
            return

        if isinstance(user, tuple):  # if user is File
            for user_i in user:  # run cycle
                if isinstance(passwd, list):  # if password is File
                    for passwd_i in passwd:  # run cycle for password
                        if self.connect(user_i, passwd_i, timeout):  # connect user_iteration password_iteration
                            return
                else:  # if password not file
                    if self.connect(user_i, passwd, timeout):  # conn user_iteration password
                        return
        else:  # if user not file
            if isinstance(passwd, list):  # if password is file
                for passwd_i in passwd:  # run cycle
                    if self.connect(user, passwd_i, timeout):  # connect user and password_iteration
                        return
            else:  # else
                if self.connect(user, passwd, timeout):  # else connect user password
                    return

    @staticmethod
    def _get_user_passwd(user: str, passwd: str):
        tmp_user: str | FileBase
        tmp_passwd: str | FileBase

        if user.split('.')[-1] == 'txt':
            tmp_user = FileBase(user)
        else:
            tmp_user = user

        if passwd.split('.')[-1] == 'txt':
            tmp_passwd = FileBase(passwd)
        else:
            tmp_passwd = passwd

        return tmp_user, tmp_passwd

    @staticmethod
    def raise_err( message: str = "Error", code: int = 0):
        print(f"{message}", tag='Error', tag_color='red')
        exit(code)


    @staticmethod
    def get_chunks(item, chunk):
        items, chunk = item, chunk
        return zip(*[iter(items)] * chunk)