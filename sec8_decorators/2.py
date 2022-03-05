# higher order function HOC
# two ways

# (1) use func as param
def greet(func):
    func()


# (2) return func
def greet2():
    def func():
        return 5
    return func
