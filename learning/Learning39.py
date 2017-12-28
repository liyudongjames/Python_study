# ThreadLocal
# 运用ThreadLocal管理线程中的局部变量

# 全局变量local_school就是一个ThreadLocal对象，每个Thread对它都可以读写student属性，但互不影响。你可以把local_school看成全局变量，
# 但每个属性如local_school.student都是线程的局部变量，可以任意读写而互不干扰，也不用管理锁的问题，ThreadLocal内部会处理。
# 可以理解为全局变量local_school是一个dict，不但可以用local_school.student，还可以绑定其他变量，如local_school.teacher等等。
# ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，
# 这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。

import threading

local_para = threading.local()


def std_student():
    std = local_para.person
    print("My name is %s , I'm in the %s" % (std, threading.current_thread().name))


def run_body(name):
    local_para.person = name
    std_student()


thread1 = threading.Thread(target=run_body, args=("David",), name="davidThread")
thread2 = threading.Thread(target=run_body, args=("Ace",), name="aceThread")
thread1.start()
thread2.start()
thread1.join()
thread2.join()