# 函数 变量可以指向一个函数


def one_plus_one(number):
    print(number + number)


def transfer(number):
    return number * 3


f = one_plus_one
f(3)
list_what = [1, 2, 3, 4, 5, 6, 7]
list_what = map(transfer, list_what)
print(list_what)
sdfs = list(map(str, [1, 2, 3, 4, 5, 6, 7]))
print(sdfs)