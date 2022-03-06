# Error handling
while True:
    try:
        age = int(input('what is your age?'))
        10/age
        raise Exception('hey cut it out.')
    # only one of the error will be caught
    except ZeroDivisionError:
        print('please enter age higher than 0')
        break  # break out of the loop
    else:
        print('Thank you!')
    # run finally regardless of everything above
    finally:
        print('ok, I am finally done.')
    print('can you hear me?')
