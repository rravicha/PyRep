class cname:
  def __init__(self,Name):
    #print("Parent")
    self.name = Name
    print(Name)
  def parent_fun(self):
    print(self.name)

class cname1(cname):
  def __init__(self,Names):
    self.names = Names
    super().__init__("Krishna")
  def child_fun(self):
    print(self.names)
child = cname1("idin")
child.child_fun()
child.parent_fun()
