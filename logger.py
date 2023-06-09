import enum
import datetime


class LogLevel(enum.Enum):
    DEBUG = 1
    INFO = 3
    ERROR = 5


class Logger:
    # 日志全局开关
    log_global_open = True

    # 打印颜色常量
    __red = "\033[31m"
    __green = "\033[32m"
    __yellow = "\033[33m"
    __blue = "\033[34m"
    # 带下划线
    __yellow_underline = "\033[1;4;33m"
    __green_underline = "\033[1;4;32m"
    # 背景颜色
    __green_background = "\033[1;4;42m"
    __end = "\033[0m"

    @staticmethod
    def log():
        """获取Logger"""
        return Logger()

    def __init__(self):
        self.log_self_open = LogLevel.INFO
        
    def has_print(self, current_level):
        return Logger.log_global_open and current_level.value >= self.log_self_open.value

    def info(self, *args):
        if not self.has_print(LogLevel.INFO):
            return
        Logger.__print_blue('【INFO ', datetime.datetime.now(), '】 --  [', *args, ']\n')

    def debug(self, *args):
        if not self.has_print(LogLevel.DEBUG):
            return
        Logger.__print_yellow('【DEBUG', datetime.datetime.now(), '】 --  [', *args, ']\n')

    def error(self, *args):
        if not self.has_print(LogLevel.ERROR):
            return
        Logger.__print_read('【ERROR', datetime.datetime.now(), '】 --  [', *args, ']\n')

    def __print_read(*args):
        print(Logger.__red, *args)

    @staticmethod
    def __print_blue(*args):
        print(Logger.__blue, *args)

    @staticmethod
    def __print_green(*args):
        print(Logger.__green, *args)

    @staticmethod
    def __print_green_underline(*args):
        print(Logger.__green_underline, *args)

    @staticmethod
    def __print_green_bg(*args):
        print(Logger.__green_background, *args)

    @staticmethod
    def __print_yellow(*args):
        print(Logger.__yellow, *args)
