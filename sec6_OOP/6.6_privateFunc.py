class PlayerCharacter:
    def __init__(self, name, age):
        self._name = name  # <<
        self._age = age  # <<

    def speak(self):
        print(f'my name is {self.name}, and I '
              f'am {self.age} years old')


player1 = PlayerCharacter('Meredith', 8)
print(player1.speak())

# The problem of not making the function private
player1.speak = 'BOOOOO'
# print(player1.speak())
print(player1.speak)  # Boooo

# there is no true private variables in python
# just add _ in front of attributes
