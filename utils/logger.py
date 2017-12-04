# 方便打印log的一个装饰器模块
import functools


def log(log_name="Yudong"):
    def detector(func):
        @functools.wraps(func)  # 经过装饰器的函数他的函数名会变成wrapper，这一行代码就是让传进来的函数名不变
        def wrapper(*args, **kwargs):  # 这里的args指的是不带key的参数如元组，kwargs是指的带key的参数，如字典
            print("#-------------------  " + log_name + " Learn to Python  ---------------------#")
            print("#   **************** Call FUNC:  && %s() && ****************" % func.__name__)
            print("#------------------------------------------------------------------#")
            print("#                                                                  #")
            print("#      " + str(func(*args, **kwargs)))
            print("#                                                                  #")
            print("#------------------------------------------------------------------#")
            print("#-------------------  " + log_name + " Learn to Python  ---------------------#\n\n")
            return func(*args)
        return wrapper
    return detector
