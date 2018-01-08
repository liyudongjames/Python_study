# contextlib 的另一种写法
from contextlib import contextmanager


class Big_Ice(object):

    def __init__(self, name):
        self.__name = name

    def say_something(self):
        print("My name is %s" % self.__name)


# 这个方法不属于Big_Ice这个类了
@contextmanager
def create_manager(name):
    print("Whats ur name")
    q = Big_Ice(name)
    yield q
    print("ok I get it")


