# error handling

def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(f'please enter numbers and the error message: {err}')


# sum('1', 2)

def sum2(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as err:
        print(err)


sum2(0, 5)
