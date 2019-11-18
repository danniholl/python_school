# Python Homework 1 - Rental Car Calculator
# Roy Crippen
# ENG 101
# Due 11/18/2019

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
