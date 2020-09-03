# subclass of Product

from product import Product


class Clothing(Product):  # says it inherits from Product
    def __init__(self, name, price, color, size):
        # pass name and price from super class
        super().__init__(name, price)
        self.color = color
        self.size = size

    def __str__(self):
        return f"{self.name} \t ${self.price} comes in {self.color}, {self.size}"
