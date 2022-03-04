class User:
    def sign_in(self):
        return 'Logged in'


class Wizard(User):  # <<
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        return f'attacking with power of {self.power}'


class Archer(User):  # <<
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f'{self.arrows} remaining')

    def attack(self):
        return (f'attacking with arrows: arrows left: {self.arrows}')

    def run(self):
        return ('run really fast')


class Hybrid(Wizard, Archer):
    def __init__(self, name, power, arrows):  # <<
        Archer.__init__(self, name, arrows)  # <<
        Wizard.__init__(self, name, power)  # <<


hb1 = Hybrid('Borgie', 50, 100)
print(hb1.run())
print(hb1.check_arrows())
print(hb1.attack())
print(hb1.sign_in())
