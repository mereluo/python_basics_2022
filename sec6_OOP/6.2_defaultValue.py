class PlayerCharacter:
    # Class Object Attribute - doesn't change
    membership = True

    def __init__(self, name="anonymous", age=19):
        if (age > 18):
            self.name = name  # self refer to player1
            self.age = age  # attributes - change

    def shout(self):  # pass self here
        print(f'my name is {self.name}')
        return 'done'

    def run(self):
        print(f'my age is {self.age}')


player1 = PlayerCharacter()

print(player1.shout())
