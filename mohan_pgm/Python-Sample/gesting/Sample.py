##class person:
##  def __init__(self, name):
##    self._name = name
##    
##  def getName(self):
##    return self._name
##  
##  def setName(self, value):
##    self._name = value
##    
##  def delName(self):
##    del self._name
##    
##  name = property(setName, getName, delName, "testing")
##
##
##
##var = person("Dhoni")
##print var.name
##
##var.name = "v kohli"
##print var.name
##
##del var.name

#------------------------------------------- finding whether number elements in the given list are same-----------------------------------

lst = ['a', 'a', 'a']

##print(len(set(lst)) == 1)
##
##print(all(x == lst[0] for x in lst))
##
print(lst[0])
print(len(lst))
print(lst.count(lst[0]) == len(lst))

####for x in lst:
####
####  if x == lst[0]:
####
####    print("element are common")
####  
  
