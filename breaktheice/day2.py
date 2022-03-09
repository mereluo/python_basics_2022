
# Question 4
# lst = input("give me a sequence of comma-separated numbers: ").split(',')
# tpl = tuple(lst)
# print(lst)
# print(tpl)


# Question 5
# class inputString():

#     def getString(self):
#         self.s = input("give me a string: ")

#     def printString(self):
#         print(self.s.upper())


# xx = inputString()
# xx.getString()
# xx.printString()

# Question 6
# from math import sqrt


# c, h = 50, 30


# def calc(D):
#     return sqrt((2*c*D)/h)


# D = [int(i) for i in input("comma-separated sequence: ").split(",")]
# D = [round(calc(i)) for i in D]
# D = [str(i) for i in D]

# print(','.join(D))

# Question 7
# coord = [int(i) for i in input("comma-separated sequence: ").split(",")]

# res = []
# for i in range(coord[0]):
#     row = []
#     for j in range(coord[1]):
#         row.append(i*j)
#     res.append(row)

# print(res)

# Question 8
# words = input("comma separated sequence: ").split(',')
# words.sort()
# print(','.join(words))

# Question 9
lst = []

while True:
    x = input()
    if len(x) == 0:
        break
    lst.append(x.upper())

for line in lst:
    print(line)
