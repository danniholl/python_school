# # Simple quick test before the assignment
# # print('\n\n\n hello world\n\n\n')


e_name = input('What is your first and last name? ')
if e_name.isdigit():
    print('That is not your name!')
    exit()


e_id = input('What is your 4 digit employee ID? ')
if len(str(e_id)) != 4 or not e_id.isdigit():
    print("Please input a valid employee ID Number!")
    exit()

h_wage = float(input('What is your hourly wage? '))
h_worked = float(input('How many hours did you work last week? '))

pay: float = h_wage * h_worked

print(e_name, 'is hourly employee: \tNumber: ' + e_id)
print(e_name, 'has worked', h_worked, 'hours last week.')
print(e_name, 'earned $' + str(pay), 'last week.')
