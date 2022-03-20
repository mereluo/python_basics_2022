import re

string = "search this inside of this text please!"

# print('search' in string)
a = re.search('this', string)
print(a.span())  # (7, 11)
print(a.start())  # 7
print(a.end())  # 11
print(a.group())  # this

print(re.search('thIs', string))  # none

pattern = re.compile('this')
c = pattern.findall(string)  # ['this', 'this']
print(c)

d1 = pattern.fullmatch(string)  # pattern == string
d = pattern.match(string)  # None
print(d)
