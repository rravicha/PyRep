# Python program to illustrate the concept
# of threading
# importing the threading module
##import threading
##import os
##def print_cube(num):
##    print("CCUbe ",num*num*num)
##    print("\n")
##    print("CUBE",os.getpid())
## 
##def print_square(num):
##    print("Square ",num * num)
##    print("\n")
##    print("Square" , os.getpid())
## 
##if __name__ == "__main__":
##    # creating thread
##    t1 = threading.Thread(target=print_square, args=(10,))
##    t2 = threading.Thread(target=print_cube, args=(10,))
## 
##    # starting thread 1
##    t1.start()
##    # starting thread 2
##    t2.start()
## 
##    # wait until thread 1 is completely executed
####    t1.join()
####    # wait until thread 2 is completely executed
####    t2.join()
##
##    print("Done!")
 #--------------------------------------------Concept of Multithreading with id values------------------------------------------------------


import threading
import os
 
def task1():
    print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
    #print("Task 1 Id \n",os.getpid())
    print("Firsttttttttttttttttttt")

 
def task2():
    print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
    #print("Task 2 Id \n",os.getpid())
    print("Secconnnnnnnnnnnnddddd")
if __name__ == "__main__":
 
    # print ID of current process
    print("ID of process running main program: {}".format(os.getpid()))
 
    # print name of main thread
    print("Main thread name: {}".format(threading.main_thread().name))
 
    # creating threads
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)  
 
    # starting threads
    t1.start()
    t2.start()
 
    # wait until all threads finish
    t1.join()
    t2.join()


#-----------------------------------------------------------------------------------------------------------------------------
