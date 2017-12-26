# 多线程

import time, threading


def loop():
    n = 0
    print("thread is start %s" % threading.current_thread().name)
    while n < 5:
        n = n+1
        print("thread running %s %d" % (threading.current_thread().name, n))
        time.sleep(1)


print("Let's test threading")
thread = threading.Thread(target=loop(), name="David Thread")
thread.start()
thread.join()
print("thread ending")

