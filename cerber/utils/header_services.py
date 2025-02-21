import json


class HeaderServices:
    headers =  {}

    @staticmethod
    def set_default():
        HeaderServices.headers.update({
            "User-Agent": "Cerber",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
        })

    @staticmethod
    def set(header_json_string: str):
        HeaderServices.headers = json.loads(header_json_string)