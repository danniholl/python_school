# Python Assignment 4
# Roy Crippen
# ENG 101
# Due 11/5/2019
#
# First I import the random and time libraries.
# Random will be used to have the computer select it's choice for rock, paper, scissors.
# Time will be used to implement code delays to make the game a bit more interesting.
import random
import time

# Here I set up a set of options for the user and computer to select from.
# I also set variables for the number of wins for each competitor to zero.
choices = ['rock', 'paper', 'scissors']
comp_wins = 0
user_wins = 0

# This while loop will loop the game until either the computer or the user wins 4 games.
while comp_wins <= 3 and user_wins <= 3:
    # Here the computer makes it's choice using the random library.
    comp_choice = choices[random.randint(0, 2)]
    # Here the user makes their choice.
    user_choice = input('Rock, Paper, or Scissors? ')

    # Here I check if the user choice is actually a valid choice and print if it is a valid choice.
    if user_choice.lower() not in choices:
        print('Please input either rock, paper, or scissors!')
    else:
        # Here I use the time library to implement delays into my code to make it slightly more interesting.
        print('Rock!')
        time.sleep(.5)
        print('Paper!')
        time.sleep(.5)
        print('Scissors!')
        time.sleep(.5)
        print('Shoot!\n')
        time.sleep(.5)

        # Here I print what the user picked and what the computer picked.
        print('You picked ' + user_choice.lower() + ', the computer picked ' + comp_choice + ':')

        # Here I assume that the user has won the game. I assume that the user has won so that I only have to check
        # the cases in which the user loses.
        user_won = True
        # Here I check to see if the user choice and computer choice are the same and print 'It's a draw!' if that is
        # true. If the user choice is not equal to the computer choice than the code continues on to the rest of the
        # logic.
        if user_choice.lower() == comp_choice:
            print('It\'s a draw!\n')
            continue
        # Here is the majority of the game logic. I only check the cases in which the user has lost.
        elif user_choice.lower() == 'rock' and comp_choice == 'paper':
            user_won = False
        elif user_choice.lower() == 'paper' and comp_choice == 'scissors':
            user_won = False
        elif user_choice.lower() == 'scissors' and comp_choice == 'rock':
            user_won = False
        # If the user has won the game than the user_wins counter will increment and then print, vise versa for
        # the computer wins.
        if user_won:
            user_wins += 1
            print('You win!\n')
        else:
            comp_wins += 1
            print('You lose!\n')

# Here I print out the final result of the game.
if user_wins == 4:
    print("You won the game!")
else:
    print("Sorry, you lost the game!")
print('\nFinal Score: \n Computer wins: {} \n User wins: {}'.format(comp_wins, user_wins))
