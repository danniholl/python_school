# Simple quick test before the assignment
# print('\n\n\n hello world\n\n\n')
import sys

e_name = input('What is your first and last name? ')
e_id = input('What is your 4 digit employee ID? ')
if len(e_id) != 4:
    sys.exit("Please input a valid employee ID Number!")

h_wage = int(input('What is your hourly wage? '))
h_worked = int(input('How many hours did you work last week? '))

pay: int = h_wage * h_worked

print(e_name, 'is hourly employee: \tNumber: {}'.format(e_id))
print(e_name, 'has worked', h_worked, 'hours last week.')
print(e_name, 'earned ${}'.format(pay), 'last week.')
