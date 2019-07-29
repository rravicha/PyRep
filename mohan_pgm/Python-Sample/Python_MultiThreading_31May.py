import threading
import time

def fun(var,delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(var, time.ctime(time.time()))

if __name__ == "__main__":
    t = threading.Thread(target = fun, args=("First",2))
    t1 = threading.Thread(target = fun, args=("Second",4))

    t.start()
    t1.start()

    t.join()
    t1.join()

#--------------------------------------------------------
##
##import threading
##import time
##
##def fun(var, lock, counter):
##    counter = 0
##    while counter < 5:
##        counter += 1
##        lock.acquire()
##        print("printing First thread counter value", counter)
##        print("priting only the first thread")
##        lock.release()
##        #time.sleep(5)
##def fun2(var, lock, counter):
##    counter = 0
##    while counter < 5:
##        counter += 1
##        lock.acquire()
##        print("printing Second thread counte value", counter)
##        print("priting only the Second thread")
##        lock.release()
##        #time.sleep(5)
##if __name__ == "__main__":
##    lock = threading.Lock()
##    t = threading.Thread(target = fun, args=("First",lock,5))
##    t1 = threading.Thread(target = fun2, args=("Second",lock,5))
##    t.start()
##    t1.start()
##    
##    t.join()
##    t1.join()


#-----------------------------------------------------------------------

import threading
import time

def fun(var, lock, counter):
    x = 0
    for _ in range(10):
        lock.acquire()
##        x = 0
        print(var)
        commonfunction(x)
        lock.release()

def commonfunction(x):
    #x = 0
    x += 1
    print(x)
##def fun2(var, lock, counter):
##    while True:
##        lock.acquire()
##        print("printing Second thread")
##        print("priting only the Second thread")
##        lock.release()
##        time.sleep(5)
if __name__ == "__main__":
    lock = threading.Lock()
    t = threading.Thread(target = fun, args=("First",lock,5))
    t1 = threading.Thread(target = fun, args=("Second",lock,5))
    t.start()
    t1.start()
    t.join()
    t1.join()

#--------------------------------------------------------------------------















