import random


def game(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('you are a genius!')
            return True
    else:
        print("the guess should between 1 and 10")
        return False


if __name__ == "__main__":

    answer = random.randint(1, 10)
    while True:
        try:
            guess = int(input('guess a number 1~10: '))
            if (game(guess, answer)):
                break
        except ValueError:
            print('please enter a number')
            continue
