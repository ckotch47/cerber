import re

import requests as req
from bs4 import BeautifulSoup

google_modes = [
    'https://www.google.com/search?q=site:{{target}}+ext:doc+|+ext:docx+|+ext:odt+|+ext:rtf+|+ext:sxw+|+ext:psw+|+ext:ppt+|+ext:pptx+|+ext:pps+|+ext:csv',
    'https://www.google.com/search?q=site:{{target}}+intitle:index.of',
    'https://www.google.com/search?q=site:{{target}}+ext:xml+|+ext:conf+|+ext:cnf+|+ext:reg+|+ext:inf+|+ext:rdp+|+ext:cfg+|+ext:txt+|+ext:ora+|+ext:ini+|+ext:env',
    'https://www.google.com/search?q=site:{{target}}+ext:sql+|+ext:dbf+|+ext:mdb',
    'https://www.google.com/search?q=site:{{target}}+ext:log',
    'https://www.google.com/search?q=site:{{target}}+ext:bkf+|+ext:bkp+|+ext:bak+|+ext:old+|+ext:backup',
    'https://www.google.com/search?q=site:{{target}}+inurl:login+|+inurl:signin+|+intitle:Login+|+intitle:%22sign+in%22+|+inurl:auth',
    'https://www.google.com/search?q=site:{{target}}+intext:%22sql+syntax+near%22+|+intext:%22syntax+error+has+occurred%22+|+intext:%22incorrect+syntax+near%22+|+intext:%22unexpected+end+of+SQL+command%22+|+intext:%22Warning:+mysql_connect()%22+|+intext:%22Warning:+mysql_query()%22+|+intext:%22Warning:+pg_connect()%22',
    'https://www.google.com/search?q=site:{{target}}+%22PHP+Parse+error%22+|+%22PHP+Warning%22+|+%22PHP+Error%22',
    'https://www.google.com/search?q=site:{{target}}+ext:php+intitle:phpinfo+%22published+by+the+PHP+Group%22',
    'https://www.google.com/search?q=site:pastebin.com%20|%20site:paste2.org%20|%20site:pastehtml.com%20|%20site:slexy.org%20|%20site:snipplr.com%20|%20site:snipt.net%20|%20site:textsnip.com%20|%20site:bitpaste.app%20|%20site:justpaste.it%20|%20site:heypasteit.com%20|%20site:hastebin.com%20|%20site:dpaste.org%20|%20site:dpaste.com%20|%20site:codepad.org%20|%20site:jsitor.com%20|%20site:codepen.io%20|%20site:jsfiddle.net%20|%20site:dotnetfiddle.net%20|%20site:phpfiddle.org%20|%20site:ide.geeksforgeeks.org%20|%20site:repl.it%20|%20site:ideone.com%20|%20site:paste.debian.net%20|%20site:paste.org%20|%20site:paste.org.ru%20|%20site:codebeautify.org%20%20|%20site:codeshare.io%20|%20site:trello.com%20%22{{target}}%22',
    'https://www.google.com/search?q=site:github.com%20|%20site:gitlab.com%20%22{{target}}%22',
    'https://www.google.com/search?q=site:stackoverflow.com%20%22{{target}}%22+',
    'https://www.google.com/search?q=site:{{target}}+inurl:signup+|+inurl:register+|+intitle:Signup',
    'https://www.google.com/search?q=site:*.{{target}}',
    'https://www.google.com/search?q=site:*.*.{{target}}',
    'https://web.archive.org/web/*/{{target}}/*',
]



class GoogleHacking:
    target = ''
    method = 0
    def hack(self, target: str, method: int):
        self.target = target
        self.method = method
        str_search = google_modes[method-1].replace('{{target}}', target)
        if method == 17:
            print(str_search)
            return
        res = self.get_request(f"{str_search}")
        try:
            print(f'Search string (click for detail): https://www.google.com/search?q={str_search}')
            soup = BeautifulSoup(res.text, "html.parser")

            tmp = soup.body.select('div#main')[0]
            for i in tmp.findAll('a', href=True):
                if str(i['href']).find(target) != -1 and i.find('h3'):
                    print(re.search(r'http[\S]*&', i['href'])[0].split('&')[0],  i.find('h3').getText())
        except Exception as e:
            print(e)
            pass

    def get_request(self, path: str):
        return req.get(path)

    def link_list(self, target: str):
        for i in google_modes:
            print(i.replace('{{target}}', target))
        return