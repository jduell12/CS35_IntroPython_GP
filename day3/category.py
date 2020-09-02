# lets create a class to hold our category data
class Category:
    def __init__(self, name, products):
        self.name = name
        self.products = products

    def __str__(self):
        catString = self.name
        if len(self.products) == 0:
            catString += "\n There are no products available"
        else:
            for i, p in enumerate(self.products):
                catString += "\n" + str(i + 1) + ": " + p + "\n"
        return catString
