# 内存读写与 StringIO 和 BytesIO

from io import StringIO

f = StringIO()
f.write("hello")
f.write("world")
what = f.getvalue()
print(what)