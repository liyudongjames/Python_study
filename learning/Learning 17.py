# 切片和高级用法

what = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(what[2:])
print(what[:2])  # 切片用法的好处在于可以很直观的看出这段切片的长度是多少
print(what[-3:])

# 三元切片，最后一个参数是间隔多少，负数表示反方向
print(what[::3])
print(what[::-1])
print(what[1:5:2])

# 给切片赋值
order = list(range(10))
order[1:3] = [23, 24, 122, 32]
print(order)
