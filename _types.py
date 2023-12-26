from enum import IntEnum


class LogLevel(IntEnum):
    NOTSET = 0
    DEBUG = 10
    INFO = 20
    WARNING = 30
    WARN = WARNING
    ERROR = 40
    FATAL = 50
    CRITICAL = FATAL
