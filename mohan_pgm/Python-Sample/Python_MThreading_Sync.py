import threading

x = 0

def increment():
    global x
    x +=1

def fun(lock):
    lock.acquire()
    increment()
    print("value of x in fun {}".format(x))
    lock.release()
def fun2(lock):
    lock.acquire()
    increment()
    print("value of x in fun2 {}".format(x))
    lock.release()

if __name__ == "__main__":

    lock = threading.Lock()

    t1 = threading.Thread(target = fun, args=(lock,))
    t2 = threading.Thread(target = fun, args=(lock,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
