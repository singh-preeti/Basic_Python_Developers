class Product:
    #constructor
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cart:
        def __init__(self):
            self.product_list = []

        #Customized functions
        def add_product(self, product):
            self.product_list.append(product)
            print(product.name, "added to cart")

        def show_bill(self):
            total = 0

            print("cart items")
            for i in self.items:
                print(i.name,"-", i.price)
                total += i.price
                print("total amount" ,total)

prod = Product("Laptop", 40000)
prod1 = Product("Mobile phone", 50000)

cart = Cart()
cart.add_product(prod)
cart.add_product(prod1)

cart.show_bill()
