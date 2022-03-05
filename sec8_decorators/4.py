

# Decorator Pattern
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('***********')
        func(*args, **kwargs)
        print('***********')
    return wrap_func


@my_decorator
def hello(string, string1):
    print(string + ' ' + string1)
    return


a = 'hello'
b = 'world'
hello(a, b)
