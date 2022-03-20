import re

pattern = re.compile(r"([a-zA-Z]).([a])")
string = "search this inside of this text please!"

a = pattern.search(string)
print(a)  # <re.Match object; span=(0, 3), match='sea'>
print(a.group())  # sea
print(a.group(1))  # s
print(a.group(2))  # a
