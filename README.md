

# Usage 
Программа для простого перебора паролей и логинов по словарю 

Флаг -bomb -w cpu_count для использования потоков cpu_count число поток процессора

poetry run cerber --host [:1] -u root -p root -m ssh -t 0.6

poetry run cerber --host [:1] -u root -p root -m ftp -t 0.6

poetry run cerber --host https://[:1]/auth -m http-post -body '{"login":"$1$","password":"$2$"}' -bomb -w 4 -u worldlist/user.txt -p worldlist/password.txt 

poetry run cerber --host [:1] -u root -p root db postgres -m psql -t 0.6

## for dev
git clone https://github.com/ckotch47/cerber.git

poetry install

poetry build - for build project

poetry run cerber


## for install package
pip install https://github.com/ckotch47/cerber/releases/download/release/cerber-x.x.x-py3-none-any.whl

or

pip install https://github.com/ckotch47/cerber/releases/download/release/cerber-x.x.x.tar.gz


