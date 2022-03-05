# def hello():
#     print('hellloooo')


# greet = hello
# del hello

# print(greet())
# # even though the name "hello" is deleted, the function still remains

def hello(func):
    """help calling out other functions"""
    func()


def greet():
    print('still here!')


a = hello(greet)

print(a)

# decorator supercharges the function
