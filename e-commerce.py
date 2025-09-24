class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def show_details(self):
        print(f"Product: {self.name}, Price:{self.price}")
class Electronics(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty
    def show_details(self):
        super().show_details()
        print(f"Warranty: {self.warranty} years")
class Clothing(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size
    def show_details(self):
        super().show_details()
        print(f"Size: {self.size}")
e = Electronics("Laptop", 6000,2)
c = Clothing("Shirt", 1200, "M")
e.show_details()
c.show_details()