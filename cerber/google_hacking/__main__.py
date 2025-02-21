from .utils.parser import m_arguments
from .src import *
from print_color import print
import pyfiglet

def main():

    arguments = m_arguments
    print(
        pyfiglet.figlet_format("cerber - gh"),
        color='c'
    )
    GoogleHacking().link_list(arguments.host)
    # todo may be rework or delete
    # if not arguments.l:
    #     GoogleHacking().hack(arguments.host, arguments.m)
    # if arguments.l:
    #     GoogleHacking().link_list(arguments.host)

