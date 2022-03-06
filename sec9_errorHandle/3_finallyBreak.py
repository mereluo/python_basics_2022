# Error handling
while True:
    try:
        age = int(input('what is your age?'))
        10/age
    # only one of the error will be caught
    except ValueError:
        print('please enter an integer')
        continue   # comes back to the top
    except ZeroDivisionError:
        print('please enter age higher than 0')
        continue  # break out of the loop
    else:
        print('Thank you!')
        break
    # run finally regardless of everything above
    finally:
        print('ok, I am finally done.')
    print('can you hear me?')
