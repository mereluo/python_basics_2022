# Error handling

while True:
    try:
        age = int(input('what is your age?'))
        10/age
        print(age)
    # only one of the error will be caught
    except ValueError:
        print('please enter an integer')
    except ZeroDivisionError:
        print('please enter age higher than 0')
    else:
        print('Thank you!')
        break
