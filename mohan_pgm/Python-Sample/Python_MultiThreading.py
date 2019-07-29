import threading

def fun1(num):
  print(num*num*num)
  print("First Function \n")

def fun2(num):
  print(num*num)
  print("Second Function \n")

if __name__ == "__main__":
  t1 = threading.Thread(target = fun1, args=(10,))
  t2 = threading.Thread(target = fun2, args=(20,))
  t1.start()
  t2.start()
