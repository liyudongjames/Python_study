# contextlib 上下文管理器
# 实现上下文管理是通过__enter__和__exit__这两个方法实现的


class little_ice(object):

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def __enter__(self):
        print('BEGIN')
        return self  # 这一句return self 非常重要，如果不加在 with as 语句中就会造成实例化对象为NONE_TYPE的问题

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print('ERROR')
        else:
            print('THE END')

    def fun_one(self):
        print("%s fun one ON!" % self.__name)

    def fun_two(self):
        print("%s fun two ON!" % self.__name)
