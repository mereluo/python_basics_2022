# Users: wizards, archers... all of them have to sign in

class User:
    def __init__(self, email):  # <<
        self.email = email

    def sign_in(self):
        return 'Logged in'
    # we don't need user attributes

# class child(parent)


class Wizard(User):  # <<
    def __init__(self, name, power, email):
        # User.__init__(self, email)  # << (1)
        super().__init__(email)  # << (2)
        self.name = name
        self.power = power

    def attack(self):
        return f'attacking with power of {self.power}'


class Archer(User):  # <<
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        return f'attacking with arrows: arrows left: {self.num_arrows}'


Merlin = Wizard('Merlin', 100, 'merlin@gmail.com')
print(Merlin.email)
print(dir(Merlin))  # << object introspection
