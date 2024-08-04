import json
import requests
from print_color import print

from cerber.api_scan.src.utils.progress_bar import ProgressBarBase


# TODO genearate param for {payeload}
# TODO get example param for route
class OpenApi:
    openapi_json = None
    paths = None
    schemas = None
    headers = {}
    server = None
    show = []
    exclude = []

    result = []

    def __init__(self, args_parser=None, success_only=False):
        self.bar = None
        self.arg = args_parser
        if 'w' not in self.arg:
            exit(1)
            return
        try:
            self.headers = json.load(open(self.arg.header))
        except Exception as e:
            if self.arg.header:
                try:
                    self.headers = json.loads(str(self.arg.header))
                except:
                    pass
            pass

        self.server = self.arg.host
        try:
            self.success_only = self.arg.s
        except:
            self.success_only = success_only

        try:
            self.show = str(args_parser.so).split(',') if args_parser.so else []
            self.exclude = str(args_parser.exc).split(',') if args_parser.exc else []
        except:
            pass

    def openapi_scan_main(self):
        if str(self.arg.w).find('http') != -1:
            try:
                self.openapi_json = json.loads(str(requests.get(self.arg.w).text))
            except Exception as e:
                print(e, color='r')
                exit(-1)
        else:
            try:
                self.openapi_json = json.load(open(self.arg.w))
            except Exception as e:
                print('not -w param', color='r')
                exit(-1)
        try:
            self.paths = self.openapi_json['paths']
            self.schemas = self.openapi_json['components']['schemas']

            self.bar = ProgressBarBase(len(self.paths.keys()), 'Scan api')

            for key in self.paths.keys():
                for method in self.paths[key].keys():
                    try:
                        ref = self.paths[key][method]['requestBody']['content']['application/json']['schema']['$ref']
                        ref = ref.split('/')[-1]
                    except Exception as e:
                        ref = None
                    if method == 'get' or method == 'delete':
                        self._get_or_delete(route=key, param=None, method=method)
                    if method == 'post' or method == 'patch' or method == 'put':
                        tmp_schemas = self.schemas[ref] if ref in self.schemas else None
                        self._post_or_patch_or_put(key, tmp_schemas, method)

                self.bar.__next__()
            self.bar.__del__()
            self._print_result()
            return
        except KeyboardInterrupt:
            print('\nExit by user', color='r')
        except TypeError:
            print('not path into parameter try -h --help', color='r')
        except Exception as e:
            print(e, color='r')
            exit(-1)

    def _get_or_delete(self, route: str, param: dict | None = None, method='get'):
        try:
            res = requests.request(
                method=method.upper(),
                url=f"{self.server}{route}",
                params=param,
                headers=self.headers)
            self.result.append([res.status_code, route, method])
        except Exception as e:
            print(e)
        return

    def _post_or_patch_or_put(self, route: str, schemas: dict | None, method='post'):
        # todo add param from schemas
        data = {}
        if schemas:
            for name in schemas.keys():
                try:
                    data[name] = schemas[name]['type']
                except:
                    pass
            try:
                res = requests.request(
                    method=method.upper(),
                    url=f"{self.server}{route}",
                    data=json.dumps(data),
                    headers=self.headers)
                self.result.append([res.status_code, route, method])
            except Exception as e:
                print(e)
            return

        res = requests.request(
            method=method.upper(),
            url=f"{self.server}{route}",
            headers=self.headers)
        self.result.append([res.status_code, route, method])
        return


    def _print_result(self):
        for i in self.result:
            self._print(i[0], i[1], i[2])

    def _print(self, status: int, route: str, method: str = ''):
        if self.show != [] and str(status) in self.show:
            self._print_color(status, route, method)
            return
        if self.exclude != [] and str(status) not in self.exclude:
            self._print_color(status, route, method)
            return
        if self.exclude == [] and self.show == []:
            self._print_color(status, route, method)

        return

    def _print_color(self,  status: int, route: str, method: str = ''):
        if status < 400:
            print(f'[{method.upper()}] {route}', tag_color='g', color='c', tag=f'{status}')
        elif status < 600:
            print(f'[{method.upper()}] {route}', tag_color='r', color='c', tag=f'{status}')