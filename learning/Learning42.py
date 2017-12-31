# 内建模块 datetime
from datetime import datetime


def get_current_time():
    return datetime.now()


print(get_current_time())
print(type(get_current_time()))


def get_time() -> datetime:
    my_time = datetime(2012, 9, 1, 9, 0)
    return my_time


print(get_time())


def get_timestamp():
    what_time = get_time().timestamp()
    print(what_time)

