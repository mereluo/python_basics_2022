class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False
        }

    def __str__(self):
        return f'{self.color}'  # you can modify the dunder method

    def __len__(self):
        return 5

    def __del__(self):
        print('deleted!')

    def __getitem__(self, i):
        return self.my_dict[i]

    def __call__(self):
        return('Yess?')


action_figure = Toy('red', 0)
print(action_figure.__str__())  # red
print(str(action_figure))  # red
print(len(action_figure))  # 5
print(action_figure())  # Yess?
print(action_figure['name'])  # Yoyo
del action_figure

# dunder methods:
# https://docs.python.org/3/reference/datamodel.html#special-method-names
