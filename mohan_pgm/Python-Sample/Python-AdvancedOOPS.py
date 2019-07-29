#INIT overriding concepts in python. Child to have additional arguments
##class cname:
##  def __init__(self,Name):
##    #print("Parent")
##    self.name = Name
##  def parent_fun(self):
##    print(self.name)
##
##class cname1(cname):
##  def __init__(self,Name,Age):
##    self.name = Name
##    self.age = Age
##    cname.__init__(self,Name)
##  def child_fun(self):
##    print(self.name,self.age)
##child = cname1("Dhoni","History")
##child.child_fun()
##child.parent_fun()

#_________________________________________________________________

#Super() class used in single inheritance for sending values to the parent without external inheritance
class cname:
  def __init__(self,var):
    self.var = var
    #print(self.var)
  def fun(self):
    print(self.var)
class cname2(cname):
  def __init__(self):
    super().__init__("forparentvar")
  def fun2(self):
    print("Child Class")

c = cname2()
c.fun()
c.fun2()
