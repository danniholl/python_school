# Python Homework 1 - Triangles sides and angles
# Roy Crippen
# ENG 101
# Due 11/18/2019

# The goal of this code is to take three sides of a triangle from a user and to compute the angles of said triangle.
from math import degrees
from math import acos

# First I will receive the sides of the triangle from the user
side_a = int(input('What is side a? '))
side_b = int(input('What is side b? '))
side_c = int(input('What is side c? '))

# Then I will compute the angles of the triangle.
ang_a = degrees(acos((side_b**2 + side_c**2 - side_a**2) / (2 * side_b * side_c)))
ang_b = degrees(acos((side_c**2 + side_a**2 - side_b**2) / (2 * side_c * side_a)))
ang_c = 180 - ang_a - ang_b

# Then I print the results
print('\nThe sides of the triangle are ' + str(side_a) + ', ' + str(side_b) + ', and ' + str(side_c)+'.')
print('The angles (in degrees) of the triangle are ' + str(ang_a) + ', ' + str(ang_b) + ', and ' + str(ang_c)+'.')
