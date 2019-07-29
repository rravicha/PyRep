class cname:
  def __init__(self,name):
    self.name =  name
  def fun(self):
    print("FirstParent", self.name)

class cname1:
  def __init__(self,age):
    self.age = age
  def fun(self):
    print("SecondParent",self.age)

class cname2(cname1,cname):
  pass
##  def fun(self):
##    print("my final class")

c = cname2(27)
c.fun()
