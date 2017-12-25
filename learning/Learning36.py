# 多进程

import os
from multiprocessing import Process

print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac: 所以这里window报错了
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

# Linux unix mac下：
# Process (876) start...
# I (876) just created a child process (877).
# I am child process (877) and my parent is 876.


# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()  # 创建进程
    p.join()
    print('Child process end.')

# 多进程问题还很多比如 进程池 pool留到以后看吧
