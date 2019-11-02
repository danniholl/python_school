# Python Assignment 3 - Part 1
# Roy Crippen
# ENG 101
# Due 11/1/2019

# First I create an empty list that will contain the square roots of the numbers 1 through 5.
# Then I take the square root of each number 1 through 5 add them to a list and then print them.
squareroots1_5 = []
for number in range(1, 6):
    square = number ** (1/2)
    squareroots1_5.append(square)
print(squareroots1_5)

# Here I create an empty list that will contain the squares of the numbers 6 through 10.
# Then I take the squares of each number 6 through 10 and add them to a list and then print them
squares6_10 = []
for number in range(6, 11):
    square = number ** 2
    squares6_10.append(square)
print(squares6_10)

# Here I combine the two lists by using the extend function.
squareroots1_5.extend(squares6_10)
print(squareroots1_5)
