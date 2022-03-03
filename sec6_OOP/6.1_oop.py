class PlayerCharacter:
    # Class Object Attribute - doesn't change
    membership = True

    def __init__(self, name, age):
        if(PlayerCharacter.membership):
            self.name = name  # self refer to player1
            self.age = age  # attributes - change

    def shout(self):  # pass self here
        print(f'my name is {self.name}')
        return 'done'

    def run(self):
        print(f'my age is {self.age}')


name = 'David'
player1 = PlayerCharacter(name, 44)
player2 = PlayerCharacter('Cindy', 21)

print(player1.name)
print(player2.age)
print(player1.shout())
print(player1.run())
print(player1.membership)
# help(player1)
