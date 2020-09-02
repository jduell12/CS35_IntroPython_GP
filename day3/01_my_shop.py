# lets import what we need and start working on a REPL
from store import Store

my_store = Store("Bob's Emporiusm", ["Food", "Beer", "Jerky"])
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
            print("Please enter a number between 1 and %d. Enter %d to quit" %
                  (len(my_store.categories), len(my_store.categories)+1))
        else:
            print("You selected %d" % (selection))
    except ValueError:
        print("Please enter a number")
