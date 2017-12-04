# Learning 14 元组拆包

try_tuple = ('try', 'tuple')
one, two = try_tuple
print(one, two)

'''
优雅的交换元素，不需要中间商介入
'''
one, two = two, one
print(one, two)

numbers = (2, 4)
a, b = divmod(*numbers)
print(a, b)
