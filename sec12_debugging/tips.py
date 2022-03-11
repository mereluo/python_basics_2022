# debugging

# linting
# ide/editor
# read errors

# pdb: pytohn debugger
import pdb


def add(num1, num2):
    pdb.set_trace()
    return num1 + num2


add(4, 'sdf')
# step: to the next line
# a: give all the variables values
