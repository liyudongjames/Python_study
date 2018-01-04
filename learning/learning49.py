# contextlib 上下文


# 传统的读取文件的方法，需要我们手动去关闭流
from OOP.little_ice import little_ice


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


little_ice_coming()
