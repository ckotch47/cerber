from print_color import print

class Logger:
    log_level = 0
    @staticmethod
    def info(text):
        if Logger.log_level >= 4:
            print(text, color='b', tag_color='b', tag='info')

    @staticmethod
    def log( text):
        if Logger.log_level >= 2:
            print(text, color='b', tag_color='b', tag='log')

    @staticmethod
    def warn(text):
        if Logger.log_level >= 1:
            print(text, color='y', tag_color='y', tag='warn')

    @staticmethod
    def error(text):
        if Logger.log_level >= -1:
            print(text, color='r', tag_color='r', tag='error')