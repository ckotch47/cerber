import random
from random import randrange


class HeaderService:
    cache_type = ['no-cache', 'no-store', 'max-age=' + str(random.randint(0, 10)),
                  'max-stale=' + str(random.randint(0, 100)),
                  'min-fresh=' + str(random.randint(0, 10)), 'notransform', 'only-if-cache']
    accept_encode = ['compress,gzip', '', '*', 'compress;q=0,5, gzip;q=1.0', 'gzip;q=1.0, indentity; q=0.5, *;q=0']
    accept_C = ['ISO-8859-1', 'utf-8', 'Windows-1251', 'ISO-8859-2', 'ISO-8859-15']
    bots = ['http://www.bing.com/search?q=%40&count=50&first=0',
            'http://www.google.com/search?hl=en&num=100&q=intext%3A%40&ie=utf-8']

    @staticmethod
    def fake_ip():
        res = ''
        while True:
            ips = [str(randrange(0, 256)) for i in range(4)]
            if ips[0] == "127":
                continue
            res = '.'.join(ips)
            break
        return res

    @staticmethod
    def get_useragent():
        file = open('worldlist/ua.txt')
        file = file.readlines()
        res: str = random.choice(file)
        return res.replace('\n', '')

    def header(self, host='http://localhost'):
        return {
            'User-Agent': self.get_useragent(),
            'Cache-Control': random.choice(self.cache_type),
            'Accept-Encoding': random.choice(self.accept_encode),
            'Keep-Alive': '42',
            'Host': host,
            'Referer': random.choice(self.bots)
        }
