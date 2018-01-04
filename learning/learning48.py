# itertools 遍历器

import itertools
import time


# 以1循环
from functools import reduce


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


# 组合循环
def cycle_chain():
    for c in itertools.chain('ACD',"DFSDF"):
        print(c)


# 分组循环
def cycle_group_by():
    for key, value in itertools.groupby('AAFABBBCCCDDD'):
        print(key, list(value))
        time.sleep(1)


# 练习题
# 计算圆周率
def cycle_pi(odd_count):
    odd_list = itertools.count(1, 2)
    odd_list2 = itertools.takewhile(lambda x: x <= (2 * odd_count - 1), odd_list)
    base_count = 4
    return reduce(lambda x, y: base_count/x + (-base_count)/y, odd_list2)


# 写法2
def pi(N):
    s = itertools.cycle([4, -4])
    return sum(map(lambda x: next(s)/x, (x for x in range(2*N)if x % 2 == 1)))


print(pi(1000))
