class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_product(self):
        print(f"Product: {self.name}")
        print(f"Price: ₹{self.price}")



class Cart:

    def __init__(self):
        self.items = []

    def add_to_cart(self, product):
        self.items.append(product)
        print(f"{product.name} added to cart")

    def show_cart(self):

        total = 0

        print("\nCart Items:")

        for item in self.items:
            print(f"{item.name} - ₹{item.price}")
            total += item.price

        print(f"Total Amount: ₹{total}")




###########main.py#######################

from ecommerce.Product import Product
from ecommerce.Cart import Cart
def main():

    # Create products
    p1 = Product("Laptop", 50000)
    p2 = Product("Mouse", 1000)

    # Display products
    p1.display_product()
    p2.display_product()

    # Create cart
    cart = Cart()

    # Add products
    cart.add_to_cart(p1)
    print("Laptop added to cart")

    cart.add_to_cart(p2)
    print("Mouse added to cart")

    # Show cart
    cart.show_cart()

    print("Cart displayed successfully")
main()


#create a project in pycharm and create a main.py file then create a python package called ecommerce and right click to package(ecommerce) create new python file
# Product and Cart 
#later import product and cart files in main which is outside of package ecommerce.
