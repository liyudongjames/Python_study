# 变量的作用范围
from utils.logger import log

a_string = "This is a global variable"


@log
def foo():
    a_string = "test"  # 1
    print(locals())


foo()
print(a_string)
