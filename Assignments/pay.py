# Python Assignment 1
# Roy Crippen
# Due 10/24/19
# ENG 101

# Goal:
# The goal of this code is to receive 4 inputs from the user, being employee name,
# employee ID, hours worked, and hourly wage, and to calculate the total pay for that week.


# The code
# First I receive the users name and check to make sure they don't type in numbers.
e_name = input('What is your first and last name? ')
if e_name.isdigit():
    print('That is not your name!')
    exit()

# Then I receive the 4 digit employee ID and check to make sure that the input given
# is exactly 4 digits and also check that they didn't try to type in any letters.
e_id = input('What is your 4 digit employee ID? ')
if len(str(e_id)) != 4 or not e_id.isdigit():
    print("Please input a valid employee ID Number!")
    exit()

# Here I receive inputs for both the hourly wage and the hours worked and convert them from
# strings into floats.
h_wage = float(input('What is your hourly wage? '))
h_worked = float(input('How many hours did you work last week? '))

# Here I calculate the pay
pay: float = h_wage * h_worked

# Here I print out the desired results
print(e_name, 'is hourly employee: \tNumber: ' + e_id)
print(e_name, 'has worked', h_worked, 'hours last week.')
print(e_name, 'earned $' + str(pay), 'last week.')
