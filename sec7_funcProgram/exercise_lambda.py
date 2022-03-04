

# square
my_list = [5, 4, 3]
print(list(map(lambda x: x**2, my_list)))

# list sorting
a = [(0, 2), (4, 3), (10, -1), (9, 9)]

# a.sort() -> sorted by the second element
a.sort(key=lambda x: x[1])
print(a)

my_dict = {
    1: 0,
    2: 10,
    5: -1,
    4: 2
}

print(dict(sorted(my_dict.items(), key=lambda item: item[1])))
