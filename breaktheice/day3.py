# Question 10
# words = input("space-separated words: ").split(' ')
# unique = list(set(i for i in words))
# unique.sort()
# print(' '.join(unique))

# Question 11
# def check(x):
#     return int(x, 2) % 5 == 0


# num = input("binary numbers: ").split(',')
# num = list(filter(check, num))
# print(','.join(num))

# Question 12

# lst = [str(i) for i in range(1000, 3001)]
# lst = list(filter(lambda i: all(ord(j) % 2 == 0 for j in i), lst))
# print(",".join(lst))

# Question 13
word = input("some letters and some numbers: ")
letter, num = 0, 0

for i in word:
    if i.isalpha():
        letter += 1
    elif i.isnumeric():
        num += 1
print(f'LETTERS {letter} \nDIGITS {num}')
