# lets write a store class with a name and categories

class Store:
    def __init__(self, name, categories):
        # attributes
        self.name = name
        self.categories = categories

    # represent class data as string for user
    def __str__(self):
        ret = self.name
        for i, c in enumerate(self.categories):
            ret += "\n " + str(i + 1) + ": " + c.name + "\n"
        ret += "\n " + str(i+2) + ": Exit \n"
        return ret

    # represent class data for developer
    def __repr__(self):
        return "Store(%s, %s )" % (self.name, self.categories)

# amazon = Store('amazon', ['clothes', 'jewlery', 'makeup'])
# print(amazon)
