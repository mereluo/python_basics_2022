# e.g., range() is a generator

# list is a iterable, not a generator

# generator is a subset of iterable

def generator_function(num):
    for i in range(num):
        yield i*2  # pauses the function and comes back


# for item in generator_function(100):
#     print(item)

g = generator_function(100)
print(g)  # <generator object generator_function at 0x7fe15ef22b30>

next(g)  # 0
next(g)  # 2
print(next(g))  # 4 (next should be smaller than 100)
