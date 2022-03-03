class PlayerCharacter:
    # Class Object Attribute - doesn't change
    membership = True

    def __init__(self, name="anonymous", age=19):
        self.name = name  # self refer to player1
        self.age = age  # attributes - change

    def shout(self):  # pass self here
        print(f'my name is {self.name}')
        return 'done'

    @classmethod
    def adding_things(cls, num1, num2):  # cls: class
        return cls('Teddy', num1 + num2)

    @staticmethod
    def adding_things2(num1, num2):  # don't care about class
        return num1 + num2


player1 = PlayerCharacter('Tom', 20)

# print(player1.adding_things(2, 3))

# class method can be used without instantiating
# print(PlayerCharacter.adding_things(2, 3))

# class method can be used to instantiate a new case
player3 = PlayerCharacter.adding_things(2, 3)
print(player3.age)
