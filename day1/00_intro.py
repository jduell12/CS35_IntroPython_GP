
# This is a comment

# lets print a string
# print("Hello, CS35!", "Some other text", "and theres more...")
# print('Hello, CS35!', "Some other text", "And there's more")
# print('Hello, world!')

# variables
# label = value
# let const var (js)
# int bool short (c)
# first_name = "Tom"
# print("Hello CS35 and", first_name)
# num = 23.87

# # f strings
# my_string = "    this is a string tom"
# print(my_string)

# print(my_string.strip())
# print(len(my_string))
# print(len(my_string.strip()))

# print(f"Hello CS35 and                {first_name}.......")
# print("something on a new line")


# collections

# create an empty list? Array
# my_list = []

# print(f'my_list is {my_list}')

# create a list with numbers 1, 2, 3, 4, 5
# lst1 = [1, 2, 3, 4, 5]

# # add an element 24 to lst1
# lst1.append(24)

# print(lst1)

# # print all values in lst2
# print(lst2)


# loop over the list using a for loop
# for i in range(len(lst1)):
#     print(lst1[i])

# while loop
# count = 0
# while count < len(lst1):
#     print(lst1[count])
#     count += 1

# List Comprehensions

# Create a new list containing the squares of all values in 'numbers'
numbers = [1, 2, 3, 4]
squares = []

# using for loop to add squares of all values in numbers
for i in range(len(numbers)):
    squares.append(numbers[i]**2)

print(numbers)
print(squares)
# Filtering with a list comprehension
evens = []

# using for loop and if statement to get even numbers
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        evens.append(numbers[i])

# create a new list of even numbers using the values of the numbers list as inputs

print(evens)

# create a new list containing only the names that start with 's' make sure they are capitalized (regardless of their original case)
names = ["Sarah", "jorge", "sam", "frank", "bob", "sandy"]
s_names = []

for i in range(len(names)):
    name = names[i].capitalize()
    if name[0] == 'S':
        s_names.append(name)

print(s_names)

# Dictionaries

# Create a new dictionary

# empty

# key value pairs

# access an element via its key
