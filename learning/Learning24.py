# 内嵌函数 和 装饰器


# __内嵌函数__
def outer(x):
    y = 2

    def inner():
        print(x, y)
    inner()


outer(4)


# __装饰器__
def log(func):
    def wrapper(*args):
        print("-------  Yudong Learn to PyThon  ---------")
        print("-------     Call FUNC:  %s()  --------" % func.__name__)
        return func(*args)
    return wrapper


@log
def now(time):
    print(time)


now("2017-11-24")
