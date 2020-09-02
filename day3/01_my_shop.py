# lets import what we need and start working on a REPL
from store import Store
from category import Category

food = Category("Food", ["jerky", "candy"])
drinks = Category(
    "Drinks", ["Beer", "Wine", "Water", "Pop"])
candy = Category("Candy", [])

my_store = Store("Bob's Emporiusm", [food, drinks, candy])
print(my_store)
# print(repr(my_store))
selection = 0

# input parser
while selection != len(my_store.categories)+1:
    selection = input(
        'Please select the number of a department or %d to quit. ' % (len(my_store.categories) + 1))
    try:
        selection = int(selection)
        if selection == len(my_store.categories) + 1:
            print("Thank you for shopping at %s" % (my_store.name))
        elif selection < 0 or selection > len(my_store.categories) + 1:
            print("Please enter a number between 1 and %d." %
                  (len(my_store.categories)))
        else:
            print(my_store.categories[selection-1])
    except ValueError:
        print("Please enter a number")
