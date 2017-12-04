import functools

print(int('123456', base=10))
int2 = functools.partial(int, base=2)
print(int2('1000010010'))
