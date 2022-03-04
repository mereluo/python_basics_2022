from functools import reduce
my_list = [1, 2, 3]


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print((reduce(accumulator, my_list, 0)))

"""
0 1     print(0, 1) return 1+0 = 1
1 2     print(1, 2) return 1+2 = 3
3 3     print(3, 3) return 3+3 = 6
6
"""
