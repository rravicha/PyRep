from functools import wraps
def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__),level=logging.INFO)
    @wraps(orig_func)
    def wrapper(*args,**kwargs):
        logging.info(
            'Ran with args:{},and kwargs:{}'.format(args,   kwargs))
        return orig_func(*args,**kwargs)
    
    return wrapper

def my_timer(orig_func):
    import time
    @wraps(orig_func)
    def wrapper(*args,**kwargs):
        t1=time.time()
        result=orig_func(*args,**kwargs)
        t2=time.time()-t1
        print(f'{orig_func.__name__} ran in {t2} sec')
        return result
    return wrapper
import time
# @my_logger
# @my_timer
def display_info(name,age):
    time.sleep(1)
    print(f'display info ran wit args: {name},{age}')

# display_info=my_logger(my_timer(display_info))
print(display_info.__name__)
display_info("Susi",2)



