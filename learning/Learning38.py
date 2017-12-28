# 线程锁
import threading

from learning import global_para

charge = 0
lock = threading.Lock()


# 不加线程锁的时候每次结果都可能不一样
def count(n):
    # global关键字表示全局变量，这是python的特性，如果不加global关键字，那么这个charge会成为一个局部变量
    # 操作global关键字还有另外一种方法，就是重新写一个文件专门管理全局变量
    global charge
    charge = charge + n
    charge = charge - n


def count_with_lock(n):
    lock.acquire()
    try:
        # global_para.count就是另外一种编写全局变量的方法，将全局变量写在global_para.py中
        global_para.count = global_para.count + n
        global_para.count = global_para.count - n
    finally:
        lock.release()


def run_thread(n):
    for i in range(100000):
        # count(n)
        count_with_lock(n)  # 加上锁每次结果都是正确的了


thread1 = threading.Thread(target=run_thread, args=(3,), name="NO.1")
thread2 = threading.Thread(target=run_thread, args=(5,), name="NO.2")
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(charge)
