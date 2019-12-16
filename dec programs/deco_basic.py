def decorator_function(func):
    def wrapper_function(*args,**kwargs):
        print('priviliges applied')
        return func(*args,**kwargs)
    return wrapper_function
class decorator_class(object):
    def __init__(self,func):
        self.func=func
    def __call__(self,*args,**kwargs):
        print('__call__ executed')
        return self.func(*args,**kwargs)
 
@decorator_class
def display():
    print('workload executing')
@decorator_class
def display_info(name,age):
    print(f'workload executing for {name}-{age}')
   

display()
display_info('susi',2)
