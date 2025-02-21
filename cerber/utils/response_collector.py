from typing import Literal

from print_color import print

class ResponseCollectorDto:
    text: str
    color: Literal["purple", "blue", "green", "yellow", "red", "magenta", "yan", "black", "white", "v", "p", "b", "g", "y", "r", "m", "c", "k", "w"] | None
    tag_color: Literal["purple", "blue", "green", "yellow", "red", "magenta", "yan", "black", "white", "v", "p", "b", "g", "y", "r", "m", "c", "k", "w"] | None
    tag: str

    def __init__(self, text, color, tag_color, tag):
        self.text = text
        self.color = color
        self.tag_color = tag_color
        self.tag = tag

class ResponseCollector:
    response: list[ResponseCollectorDto] = []
    format: Literal["csv"] | None = None

    @staticmethod
    def print_response():
        for i in ResponseCollector.response:
            if ResponseCollector.format is None:
                print(i.text, color=i.color, tag_color=i.tag_color, tag=i.tag)
            else:
                print(i.tag, i.text)