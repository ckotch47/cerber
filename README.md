## for dev
git clone https://github.com/ckotch47/opeapi-scan.git

poetry install

poetry build - for build project

## run 
use -bomb -w cpu_count для использования потоков  

poetry run cerber --host [:1] -u root -p root -m ssh -t 0.6

poetry run cerber --host [:1] -u root -p root -m ftp -t 0.6

poetry run cerber --host https://[:1]/auth -m http-post -body '{"login":"$1$","password":"$2$"}' -bomb -w 4 -u worldlist/user.txt -p worldlist/password.txt 

poetry run cerber --host [:1] -u root -p root db postgres -m psql -t 0.6
