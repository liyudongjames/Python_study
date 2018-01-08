# contextlib 上下文


# 传统的读取文件的方法，需要我们手动去关闭流
from contextlib import contextmanager
from contextlib import closing
from urllib.request import urlopen

from OOP.little_ice import little_ice
from OOP.big_ice import create_manager

def read_file_manual():
    try:
        f = open('D:/python_project/text', 'r', encoding='UTF-8')
        print(f.readline())
    finally:
        if f:
            f.close()


# 利用with as 语法打开文件，省去了我们手动关闭流的操作，open函数返回的fp对象能够使用with as 语法
# 我们也可以写一个可以嵌套在with as语句中的类
# 实现了上下文管理（contextlib）的类都可以嵌套with as语句的
def read_file_auto():
    with open('D:/python_project/text', 'r', encoding='UTF-8') as f:
        print(f.readline())


def little_ice_coming():
    with little_ice('QQ小冰') as xiaobing:
        xiaobing.fun_one()


# with as 的另外一种写法，不用通过写 enter 和 exit 方法也可以实现with as
# 通过contextmanager注解
def big_ice_coming():
    with create_manager("QQ 大兵") as what:
        what.say_something()


# 也可以用contextmanager来使调用一个方法之前和之后进行特定的操作
@contextmanager
def decorate():
    print("<h>")
    yield
    print("</h>")


def target():
    with decorate():
        print("i am a decorate")


# closing 的实现自动将一个方法变成一个contextmanager类型
# 在执行完函数的最后执行closing语句，实现很简单具体可以看下源码
def thing():
    with closing(urlopen('http://www.baidu.com')) as page:
        for line in page:
            print(line)


thing()
big_ice_coming()
target()
