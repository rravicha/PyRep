import os

#print(os.environ())
#print(os.getcwd())
def fun(var):
    print(var)
    print(os.getpid())
def fun1(var1):
    print(var1)
    print(os.getpid())

fun("Dhoni")
fun1("kohli")
print(os.getpid())
