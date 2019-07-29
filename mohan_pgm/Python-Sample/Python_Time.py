import time

##localtime = time.localtime(time.time()) 
##print(localtime)


localtime = time.asctime(time.localtime(time.time()))
print(localtime)
