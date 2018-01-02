# itertools 遍历器

import itertools
import time


# 以1循环
def cycle_num():
    natural = itertools.count(1)
    # 下面是一个无限循环，按住ctrl c停止
    for n in natural:
        print(n)
        time.sleep(1)


# 循环指定列表，字符串
def cycle_ABC():
    natural = itertools.cycle('ABC')
    # 下面是一个无限循环，按住ctrl c停止
    for n in natural:
        print(n)
        time.sleep(1)


# 循环3次
def cycle_three_times():
    natural = itertools.repeat('D', 3)
    for n in natural:
        print(n)
        time.sleep(1)


# 循环10次中断判断 takewhile
def cycle_interrupted():
    natuals = itertools.count(1)
    ns = itertools.takewhile(lambda x: x <= 10, natuals)
    for n in ns:
        print(n)
        time.sleep(1)


cycle_interrupted()
