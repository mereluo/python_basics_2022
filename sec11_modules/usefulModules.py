from collections import Counter, defaultdict, OrderedDict

# Counter
li = [1, 2, 3, 4, 5, 6, 7, 7]
print(Counter(li))
print(li.count(7))

sentence = 'blah blah python'
print(Counter(sentence))

# defaultdict
my_dict = defaultdict(int, {'a': 1, 'b': 2})
print(my_dict['a'])
print(my_dict['c'])
print(int())
my_dict = defaultdict(lambda: 5, {'a': 1, 'b': 2})
print(my_dict['c'])

# OrderedDict
d3 = OrderedDict()
d3['a'] = 1
d3['b'] = 2

d4 = OrderedDict()
d4['b'] = 2
d4['a'] = 1

print(d3 == d4)

# ordinary dict does not care about the order of inputs
d = {}
d['a'] = 1
d['b'] = 2

d1 = {}
d1['b'] = 2
d1['a'] = 1

print(d == d1)
