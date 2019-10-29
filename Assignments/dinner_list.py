# Python Assignment 2
# Roy Crippen
# ENG 101
# Due 10/29/2019

# Part 1 - Create a list of 3 people in order of priority, a time, and a place
# Here I create my initial list of people in order of priority, I also create a time and a place.
guests = ['Bill', 'Joe', 'Jeb']
location = 'Charger Union'
time = 'Friday, October 28th at 7 pm'

# Part 2 - Print evite messages to the guests
# Here I concatenate each variable and index from the list together to create the evite message.
print(guests[0]+' you are invited to dinner at '+location+' on '+time+'.')
print(guests[1]+' you are invited to dinner at '+location+' on '+time+'.')
print(guests[2]+' you are invited to dinner at '+location+' on '+time+'.')

# Part 3 - Joe Cannot make it and we need to add someone else to the list and invite them.
# Here I delete Joe from the list and insert Mary in his place
# I then send Mary an invitation
del guests[1]
guests.insert(1, 'Mary')
print(guests[1]+' you are invited to dinner at '+location+' on '+time+'.')

# Part 4 - The dinner table is bigger and we must add 3 guests of varying priority
# First I add Dr. English to the list in the highest priority position.
# I then print out her invitation.
guests.insert(0, 'Dr. English')
print(guests[0]+' you are invited to dinner at '+location+' on '+time+'.')
# Here I add Ben to the middle of the list and Mark to the end of the list.
guests.insert(2, 'Ben')
guests.insert(5, 'Mark')
# Here I print out Ben and Mark's invitations.
print(guests[2]+' you are invited to dinner at '+location+' on '+time+'.')
print(guests[5]+' you are invited to dinner at '+location+' on '+time+'.')

# Part 5 - I suck and lost 2 chairs, must remove the last two people and apologize
# Here I pop the second to last element of the list twice and store each element into their own variables.
# I pop the second to last element twice because the second to last element will become the last element
# after I pop it once and since I need both the last element and the second to last element popping it twice
# will give me the desired results.
removeguest1 = guests.pop(4)
removeguest2 = guests.pop(4)
# I then print out the apology message.
print('I\'m sorry '+removeguest1+', but you can\'t come to my house for dinner.')
print('I\'m sorry '+removeguest2+', but you can\'t come to my house for dinner.')
