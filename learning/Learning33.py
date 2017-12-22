#  操作文件和目录

import os
import platform

# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
print(os.name)
# 获取操作系统详细信息
print(platform.uname())
# 环境变量
print(os.environ)
# 获取绝对路径
print(os.path.abspath('.'))
# 创建文件夹
os.mkdir("test")
# 删除文件夹
os.rmdir('test')

# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。在Linux/Unix/Mac下，os.path.join()返回这样的字符串：
# part-1/part-2
# 而Windows下会返回这样的字符串：
# part-1\part-2

# 列出所有.py的文件
pylist = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
print(pylist)
