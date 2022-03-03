class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
Cat1 = Cat('mewo', 2)
Cat2 = Cat('mimi', 5)
Cat3 = Cat('ball', 1)

# 2 Create a function that finds the oldest cat


def get_oldest_cat(*args):
    return max(args)

# 3 Print out: "The oldest cat is x years old.".
# x will be the oldest cat age by using the function in #2


print('The oldest cat is '
      f'{get_oldest_cat(Cat1.age, Cat2.age, Cat3.age)}'
      ' years old')
