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

print(player1.name)  # David
print(player2.age)  # 21
print(player1.shout())  # my name is David done
print(player1.run())  # my age is 44 None
print(player1.membership)  # True
# help(player1)
