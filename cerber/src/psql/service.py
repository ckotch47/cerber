from cerber.src.utils import CerberBase
from print_color import print
import psycopg


class PsqlCerber(CerberBase):
    def __init__(self, host: str, db_name: str = 'postgres', debug=False):
        self.db = db_name
        super().__init__(host, debug)

    def connect(self, user: str, passwd: str, timeout: float):
        try:
            psycopg.connect(f"postgresql://{user}:{passwd}@{self.host}:{self.port}/{self.db}")
            print(f"{user}:{passwd}", tag='success', tag_color='green')
        except Exception as e:
            if self.debug:
                print(f"{user}:{passwd}", tag='fail', tag_color='red')
            return None
