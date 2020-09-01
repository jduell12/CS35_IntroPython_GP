# Return the "centered" average of an array of ints, which we'll say is the mean average of the values,
# except ignoring the largest and smallest values in the array (list).

# what do we do if smallest or largest is duplicated
# - we only consider 1 of smallest and 1 of largest to be valid

# what data type are we expecting to return?
# int / float?
# return an int

# centered_average([1, 2, 3, 4, 100]) → 3 >>> [2, 3, 4, 100] -> [2, 3, 4] -> 2 + 3 + 4 => 9 / 3 => 3
# centered_average([1, 1, 5, 5, 10, 8, 7]) → 5 >>> [1, 5, 5, 10, 8, 7] -> [1, 5, 5, 8, 7] -> 1 + 5 + 5 + 8 + 7 => 26 / 5
# centered_average([-10, -4, -2, -4, -2, 0]) → -3 >>> [-4, -2, -4, -2, 0] -> [-4, -2, -4, -2]  => -4 + -2 + -4 + -2 => -12 / 4 => -3

# centered_average([1, 2, 3, 4, 100]) -> 3 >>> [1, 2, 3, 4, 100] -> 1 + 2 + 3 + 4 + 100 => 110 => 110 - max => 10 - min => 9 / 3 => 3
# max = 100
# min = 1

# my solution
# def centered_average(listNums):
#     #makes sure not to change original list
#     listToChange = []
#     for i in range(len(listNums)):
#         listToChange.append(listNums[i])
#     # sorts the list so we can get the smallest and largest easily
#     listToChange.sort()
#     # removes minimum number from list
#     listToChange.pop(0)
#     # removes max number from list
#     listToChange.pop(len(listToChange)-1)
#     # adds the remaining numbers together
#     sum = 0
#     for i in range(len(listToChange)):
#         sum += listToChange[i]
#     print(int(sum/len(listToChange)))


# numbers = [1, 1, 5, 5, 10, 8, 7]
# centered_average(numbers)
# print(numbers)


# guided solution
# pseudocode - language agnostic and as simple as possible
"""
1. Take numbers from list and add them together after extrapolating the smallest and largest numbers to their own variables
2. Take the sum of the numbers and minus the max of the list
3. Take what is left and minus the min of the list

get the smallest value from the list
get the largest value from the list

make a sum / counter variable and set it to zero
loop over each number in our list
    sum up all of the numbers 

use the algorithm(sum = sum - largest - smallest)
apply the algorithm of sum divided by the length of our list minus 2 
"""


import statistics


def centered_avg(ints):
    minNum = min(ints)
    maxNum = max(ints)

    sum = 0

    for i in range(len(ints)):
        sum += ints[i]

    sum = sum - maxNum - minNum

    # // will give integer if it would have been a float
    return sum // (len(ints)-2)


numbers = [-10, -4, -2, -4, -2, 0]
print(centered_avg(numbers))
print(numbers)

# using methods - per lecture takes 30-40% slower


def centered_average(ints):
    ints.sort()
    return int(statistics.mean(ints[1:-1]))


numbers = [1, 3, 2, 7, 9, 0]
print(centered_average(numbers))
print(numbers)
