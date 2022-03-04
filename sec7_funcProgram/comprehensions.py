# list, set, dictionary

# my_list = [char for char in interable]

my_list = [char for char in 'hello']
print(my_list)
my_list1 = [num * 2 for num in range(0, 10)]
print(my_list1)
my_list2 = [num ** 2 for num in range(0, 10) if num % 2 == 0]
print(my_list2)

# set

my_set = {char for char in 'hello'}
print(my_set)
my_set1 = {num * 2 for num in range(0, 10)}
print(my_set1)


# dic
simple_dict = {
    'a': 1,
    'b': 2
}

my_dict = {key: value**2 for key, value in simple_dict.items()}
print(my_dict)

simple_li = [(1, 0), (3, 4)]
my_dict1 = {key: value**2 for key, value in simple_li}
print(my_dict1)

my_dict2 = {num: num*2 for num in [1, 2, 3]}
print(my_dict2)
