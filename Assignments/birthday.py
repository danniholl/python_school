# Python Assignment 3 - Part 2
# Roy Crippen
# ENG 101
# Due 11/1/2019

# Here I request the birth month of the user and then check if they capitalized the first letter.
# If they didn't capitalize the first letter I create a new variable that contains the capitalized
# version of their birth month.
birth_month = input("What is your birth month? ")
if birth_month.capitalize() != birth_month:
    birth_month_capitalized = birth_month.capitalize()

# Here I create different lists which contain the months of each season.
spring = ['March', 'April', 'May']
summer = ['June', 'July', 'August']
autumn = ['September', 'October', 'November']
winter = ['December', 'January', 'February']

# Here I check to see if the capitalized birth month is in the season of Spring
# and then print the appropriate month and number of days within that birth month.
if birth_month.capitalize() in spring:
    if birth_month.capitalize() == 'March':
        number_days = 31
        print(birth_month.capitalize()+' is in Spring and has '+str(number_days)+' days.')
    if birth_month.capitalize() == 'April':
        number_days = 30
        print(birth_month.capitalize()+' is in Spring and has '+str(number_days)+' days.')
    if birth_month.capitalize() == 'May':
        number_days = 31
        print(birth_month.capitalize()+' is in Spring and has '+str(number_days)+' days.')

# Here I check to see if the capitalized birth month is in the season of Summer
# and then print the appropriate month and number of days within that birth month.
if birth_month.capitalize() in summer:
    if birth_month.capitalize() == 'June':
        number_days = 30
        print(birth_month.capitalize()+' is in Summer and has '+str(number_days)+' days.')
    if birth_month.capitalize() == 'July':
        number_days = 31
        print(birth_month.capitalize()+' is in Summer and has '+str(number_days)+' days.')
    if birth_month.capitalize() == 'August':
        number_days = 31
        print(birth_month.capitalize()+' is in Summer and has '+str(number_days)+' days.')

# Here I check to see if the capitalized birth month is in the season of Autumn
# and then print the appropriate month and number of days within that birth month.
if birth_month.capitalize() in autumn:
    if birth_month.capitalize() == 'September':
        number_days = 30
        print(birth_month.capitalize() + ' is in Autumn and has ' + str(number_days) + ' days.')
    if birth_month.capitalize() == 'October':
        number_days = 31
        print(birth_month.capitalize() + ' is in Autumn and has ' + str(number_days) + ' days.')
    if birth_month.capitalize() == 'November':
        number_days = 30
        print(birth_month.capitalize() + ' is in Autumn and has ' + str(number_days) + ' days.')

# Here I check to see if the capitalized birth month is in the season of Winter
# and then print the appropriate month and number of days within that birth month.
if birth_month.capitalize() in winter:
    if birth_month.capitalize() == 'December':
        number_days = 31
        print(birth_month.capitalize() + ' is in Winter and has ' + str(number_days) + ' days.')
    if birth_month.capitalize() == 'January':
        number_days = 31
        print(birth_month.capitalize() + ' is in Winter and has ' + str(number_days) + ' days.')
    if birth_month.capitalize() == 'February':
        number_days = 28
        print(birth_month.capitalize() + ' is in Winter and has ' + str(number_days) + ' days.')
