##var = [['a','b'],['c','d'],['e','f']]
##var1 = list(var)
##
##print(var)
##print(var1)
##
##var.append(['india'])
##
##
##print(var)
##print(var1)
##
##
###Modifying copied object from the list
##
##var[0][1] = "inga dhan change"
##
##
##print(var)
##print(var1)

#-------------------------------------------------------------

import copy
#Deep Copy is going to have indepdent object references

var = [['a','b'],['c','d'],['e','f']]
var1 = copy.deepcopy(var)


print(var)
print(var1)

#After the Change

var[0][1] = "inga dhan change"

print(var)
print(var1)


##Note:

##1. Making a shallow copy of an object won’t clone child objects. Therefore, the copy is not fully independent of the original.
##2. A deep copy of an object will recursively clone child objects. The clone is fully independent of the original, but creating a deep copy is slower.
##3. You can copy arbitrary objects (including custom classes) with the copy module
