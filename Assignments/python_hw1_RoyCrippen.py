# Python Homework 1
# Roy Crippen
# ENG 101
# Due 11/18/2019

# I combined all of the files to reduce the number of files you will receive. If you would prefer to grade separated
# files for each problem, I would be more than happy to upload them, just message me on canvas. I would go ahead and
# upload them, but that would defeat the entire purpose of combining them.

from math import degrees
from math import acos
from decimal import Decimal

# PROBLEM 1 - The triangle calculator
# The goal of this code is to take three sides of a triangle from a user and to compute the angles of said triangle.
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
print('The angles (in degrees) of the triangle are ' + str(ang_a) + ', ' + str(ang_b) + ', and ' + str(ang_c)+'.\n\n\n')


# PROBLEM 2 - The Richter calculator
# The goal of this code is to calculate and display the amount of energy in joules and in tons of exploded TNT for
# particular Richter scale values.

# Setting up the list of richter values
rs = [1.0, 5.0, 9.1, 9.2, 9.5]

# First I calculate the energy in joules and format the output, then I calculate the equivalent amount of energy in
# tons of TNT and format that output as well. Then I print the output.
for r in rs:
    e = '%.5E' % Decimal(10**((1.5*r)+4.8))
    tnt = '%.5E' % Decimal(float(e) / (4.184*10**9))
    print('For Richter value '+str(r)+', the energy released is '+str(e)+' Joules.')
    print('The equivalent energy released in tons of TNT is '+str(tnt)+' tons of tnt.\n')
print('\n\n\n')


# PROBLEM 3, the rental car calculator
# First I will receive input from the user and check if they used a valid input.
code = input('What is your classification code? ')
valid_codes = ['b', 'B', 'd', 'D']
if code not in valid_codes:
    print('Please input a valid classification code! Program will now exit!')
    exit()

# I didn't error check for days, odo_start, and odo_finish because the int function will deal with non-integer inputs
# for me. I also go ahead and calculate the average mileage which will be used for the daily plan.
days = int(input('How many days was the vehicle rented? '))
odo_start = int(input('What was the odometer reading before rental? '))
odo_end = int(input('What was the odometer reading after rental? '))
avg_mileage = (odo_end - odo_start)/days

valid_codes = ['b', 'B', 'd', 'D']
if code not in valid_codes:
    print('Please input a valid classification code!')
    exit()

# Here I check if the customer is on the budget plan and calculate accordingly.
if code is 'b' or code is 'B':
    price = (days * 40) + (.25 * (odo_end - odo_start))
    print('You will be billed $'+str(price)+' for your rental of the vehicle.')

# Here I check if the customer is on the daily plan and calculate accordingly.
if code is 'd' or code is 'D':
    if avg_mileage >= 100:
        price = (days * 60) + ((avg_mileage - 100) * .25)
        print('You will be billed $' + str(price) + ' for your rental of the vehicle.')
    else:
        price = (days * 60)
        print('You will be billed $' + str(price) + ' for your rental of the vehicle.')
