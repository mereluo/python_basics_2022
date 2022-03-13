# Question 14
sentence = str(input("give me a sentence:  "))
upper, lower = 0, 0

for s in sentence:
    lower += s.islower()
    upper += s.isupper()

print(f'UPPER CASE {upper}\nLOWER CASE {lower}')

# Question 15

a = input('give a digit: ')
total = int(a) + int(2*a) + int(3*a) + int(4*a)
print(total)
