# Learning 13 列表推导

abc = 'abcdefghijklmn'
what = [ord(x) for x in abc]
print(what)

symbols = '$%#&@#(*$'
ok = tuple(ord(symbol) for symbol in symbols)
print(ok)
