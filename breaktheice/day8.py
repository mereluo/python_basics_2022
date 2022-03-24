# Question 22
string = input('type a string:  ').split(' ')

word = sorted(set(string))

for i in word:
    print("{0}:{1}".format(i, string.count(i)))

# succinct method
# from collections import Counter

# ss = input().split()
# ss = Counter(ss)         # returns key & frequency as a dictionary
# ss = sorted(ss.items())  # returns as a tuple list

# for i in ss:
#     print("%s:%d"%(i[0],i[1]))

# Question 23


def square(num):
    return num ** 2


# Question 24
print(str.__doc__)
print(sorted.__doc__)


def pow(n, p):
    '''
    param n: This is any integer number
    param p: This is power over n
    return:  n to the power p = n^p
    '''

    return n**p


print(pow(3, 4))
print(pow.__doc__)

# Question 25


class Car:
    # define the class parameter "name"
    name = "Car"

    def __init__(self, name=None):
        # self.name is the instance parameter
        self.name = name


honda = Car("Honda")
print("%s name is %s" % (Car.name, honda.name))

toyota = Car()
toyota.name = "Toyota"
print("%s name is %s" % (Car.name, toyota.name))
