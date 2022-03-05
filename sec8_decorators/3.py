# Decorator


def my_decorator(func):
    def wrap_func():
        print('*******')
        func()
        print('*******')
    return wrap_func


@my_decorator
def hello():
    print('hello')


@my_decorator
def bye():
    print('bye')


# underneath the hood
# a = my_decorator(hello)
# a()
hello()
bye()
