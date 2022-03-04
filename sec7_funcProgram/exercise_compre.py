some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

print(list({x for x in some_list if some_list.count(x) > 1}))
