from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        res = fn(*args, **kwargs)
        t2 = time()
        print(f'the runtime is {t2-t1} s.')
        return res
    return wrapper


@performance
def long_time():
    print('1')
    for i in range(1000000):
        i*5


@performance
def long_time2():
    print('2')
    for i in list(range(1000000)):
        i*5


long_time()  # 0.0757 s
long_time2()  # 0.1032 s
