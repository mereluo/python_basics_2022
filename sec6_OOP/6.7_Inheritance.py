# Users: wizards, archers... all of them have to sign in

class User:
    def sign_in(self):
        return 'Logged in'
    # we don't need user attributes

# class child(parent)


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        return f'attacking with power of {self.power}'


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        return f'attacking with arrows: arrows left: {self.num_arrows}'


wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)
print(wizard1.sign_in())
print(wizard1.attack())
print(archer1.attack())

print(isinstance(wizard1, User))
print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, object))  # base class python comes with
