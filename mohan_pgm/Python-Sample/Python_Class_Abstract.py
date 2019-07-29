from abc import ABC, abstractmethod
 
class AbstractClassExample(ABC):
 
    def __init__(self, value):
        self.value = value
        super().__init__()
    
    @abstractmethod
    def do_something(self):
        pass
    
class DoAdd42(AbstractClassExample):
  pass
##    def do_something(self):
##        return self.value + 42

   
x = DoAdd42(10)

print(x.do_something())


#------------------------------------Overiding abstract base class in the child ----------------------------------------------------------
##
##from abc import ABC, abstractmethod
## 
##class class1(ABC):
## 
##    def __init__(self, value):
##        self.value = value
##        super().__init__()
##    
##    @abstractmethod
##    def fun(self):
##        print("Parent Base Class")
##    
##class class2(class1):
##    def fun(self):
##        super().fun()
##        print("my inherited abstract class")   
##x = class2(10)
##x.fun()

#------------------------------------------------------------

# Note:
# 1. Abstract class is to defined a empty abstract function in the base class
# 2. Every class wich inherits the base class should have the implementation of abstract function in the code
# 3. We can have value for the base abstract class but we need to do overriding in the child class (super().fun())
