# Question 18
import re

password = input("type your password here:  ").split(',')
pat = re.compile(r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[$#@]).{6,12}$")

for s in password:
    if pat.fullmatch(s):
        print(s)

# Question 19
# result = []
# while True:
#     action = int(input("if you want to proceed, press 1  "))
#     if action == 1:
#         lst = tuple(input("name, age, score:  ").split(','))
#         result.append(lst)
#     else:
#         for i in range(3):
#             result.sort(key=lambda x: x[i], reverse=True)
#         print(result)
#         break

lst = []
while True:
    s = input().split(',')
    if not s[0]:                          # breaks for blank input
        break
    lst.append(tuple(s))

lst.sort(key=lambda x: (x[0], int(x[1]), int(x[2])))
# here key is defined by lambda and the data is sorted by element
# priority 0>1>2 in accending order
print(lst)
