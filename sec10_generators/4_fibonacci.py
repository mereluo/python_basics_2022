
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
def fib(number):
    # generator: 0, 1, 0+1, 1+1
    res = [0, 1]
    if number <= 1:
        return res[number]
    else:
        for i in range(1, number):  # 2
            new = sum(res)
            res[0] = res[1]
            res[1] = new
            i += 1
        return res[1]


@performance
def fib2(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp+b


for x in fib2(20):
    print(x)

print(fib(19))
