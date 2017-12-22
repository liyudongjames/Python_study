# 文件IO读写

try:
    f = open('io_test', 'r', encoding='UTF-8')
    io_test = f.read() # 还有readlines 返回一个list
except IOError:
    print("IOError")
finally:
    f.close()

print(io_test)

# 通过with语句自动调用close方法
with open('io_test', 'r', encoding='UTF-8') as f:
    print(f.read())

f = open('io_test', 'w', encoding='UTF-8')
f.write("hello my friend")
f.close()

with open('io_test', 'w', encoding='UTF-8') as f:
    f.write("again agian")