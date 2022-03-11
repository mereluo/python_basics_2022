import sys
import random

ans = random.randint(int(sys.argv[1]), int(sys.argv[2]))

guess = int(
    input(f"give me an integer between {sys.argv[1]} and {sys.argv[2]} "))
i = 0


while guess != ans:
    if guess < ans:
        guess = int(input("too small, guess again "))
    else:
        guess = int(input("too big, guess again "))
    i += 1
print(f"you used {i} time(s) to guess it right.")
