# Question 20
from math import sqrt


class MyGen():
    def by_seven(self, n):
        for i in range(0, int(n/7+2)):
            yield i * 7


divisible = MyGen()
generator = divisible.by_seven(int(input("Insert a number please:  ")))
for num in generator:
    print(num)

# Question 21
x, y = 0, 0
distance = 0

while True:
    move = input("direction and steps:   ").split(' ')
    if not move[0]:
        break
    elif move[0] == 'up':
        y += int(move[1])
    elif move[0] == 'down':
        y -= int(move[1])
    elif move[0] == "left":
        x -= int(move[1])
    elif move[0] == "right":
        x += int(move[1])
    distance = round(sqrt(x ** 2 + y ** 2))
    print(distance)
