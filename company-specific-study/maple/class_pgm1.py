'''
what is a class
'''
class Computer:
  
    def __init__(ragz,obj_type):
    	ragz.TYPE=('Laptop','PC','Raspian','Tablet','Mobile')
    	ragz.obj_type=obj_type
    def config(ragz):
        if ragz.obj_type in ragz.TYPE:
        	print("Valid TYPE")
        else:
        	print("Invalid TYPE")
    def compare_ot(self,cmp_obj):
    	result = True if self.obj_type == cmp_obj.obj_type else False
    	return(result)
    	# if self.obj_type==cmp_obj.obj_type:
    	# 	return True
    	# else:
    	# 	return False
obj1=Computer("PC")
obj2=Computer("Mobile")
obj3=Computer("PC")

result1=obj1.compare_ot(obj2)
print(result1)

result2=obj1.compare_ot(obj3)
print(result2)



# obj1=Computer("PC")
# obj1.config()
# Computer.config(obj1)
# print((obj1))

