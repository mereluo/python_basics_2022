# Question 1

# generator and list comprehension
print(*(i for i in range(2000, 3201) if i % 7 == 0 and i % 5 != 0), sep=",")


# Question 2
num = int(input("Enter a number: "))
res = 1
for i in range(1, num+1):
    res *= i

print(res)

# Question 3
n = int(input("give me an integer: "))
my_dict = {}
for i in range(1, n+1):
    my_dict[i] = i * i

print(my_dict)
