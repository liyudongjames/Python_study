# 偏函数


# -----偏函数的概念-------
import functools

from utils.logger import log

number_str = '123456'
number_str2 = '010100101'

# 我们想让int函数转换16进制就需要写上base参数，但是每次写上base参数会很麻烦，偏函数诞生
print(int(number_str))
print(int(number_str, base=16))
print(int(number_str2, base=2))


# 定义一个偏函数
def int2(what):
    return int(what, base=16)


print(int2(number_str))


# ----------functools.partial-------------
# -------运用functools中的函数创建偏函数------
int3 = functools.partial(int, base=2)
print(int3(number_str2))


# PS:关于functools.partial的一些其他知识

# 可以用**kw这个参数代替字典参数
kw = {'base': 2}
int4 = functools.partial(int, **kw)
print(int4(number_str2))

# 实际上会把10作为*args的一部分自动加到左边，也就是：
max2 = functools.partial(max, 10)
print(max2(5, 6, 7))

# 相当于
# ----------------------
# args = (10, 5, 6, 7) |
# max(*args)           |
# ----------------------
