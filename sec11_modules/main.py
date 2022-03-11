from utility import multiply, divide
from shopping.more_shopping import shopping_cart

if __name__ == '__main__':
    print(multiply(1, 2))
    print(divide(2, 4))
    print(shopping_cart.buy('apple'))
    print(__name__)  # __main__ is the file that is running
