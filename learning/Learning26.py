# python中的函数指针（函数指针是我说的）
# 在python中函数也是对象
from utils.logger import log


def add(x, y):
    return x + y


def minus(x, y):
    return x - y


@log(log_name='David and Ace')
def pointer_func(func, x, y):
    return func(x, y)


pointer_func(add, 3, 4)
pointer_func(minus, 7, 4)
print(pointer_func.__name__)
