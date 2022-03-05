# Why do we need decorators?
from time import time


def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'this function took {t2-t1} s')
        return result
    return wrapper


@performance
def long_time():
    for i in range(10**5):
        i*5


long_time()
