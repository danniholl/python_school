# Python Assignment 5
# Roy Crippen
# ENG 101
# Due 11/12/2019

# The Caesar Cipher The goal of this code is to take a plaintext word and shift value from a user and to shift their
# word by the shift value. For example: input = ('abc', 3) , output = 'def'. The results will be achieved by using
# lists and dictionaries.

# Here I import the string library
import string

# Here I set up a list of all the lowercase letters in the English alphabet.
x = string.ascii_lowercase
letters = list(x)

word = input('Give me a plaintext word. ')                          # First I receive the word from the user
word = word.lower()                                                 # Then I convert the word to all lowercase
if word == '' or any(str.isdigit(i) for i in word):                 # Error checking for empty input or numbers
    print('\n\nPlease enter only alphabetical characters.')         # Printing the error statement
    exit()                                                          # Exiting the program
shift = int(input('\nHow many letters would you like shifted? '))   # Receive the shift amount and convert to int

if shift < 1 or shift > 25:                                         # Restricting the input for the shift
    print('\n\nPlease use shift values between 1 and 25.')          # Printing the error statement
    exit()                                                          # Exiting the program

shifted_letters = []                                                # This will be the list of shifted letters
for letter in letters:                                              # Setup a for loop for each letter in letters
    shift_coord = ord(letter) + shift                               # Convert letter to unicode and apply the shift
    if shift_coord > 122:                                           # Check if the unicode value is above alphabet
        shift_coord = shift_coord - 26                              # Wrap back to beginning of alphabet
    shift_letter = chr(shift_coord)                                 # Converting the shifted character back from unicode
    shifted_letters.append(shift_letter)                            # Add the shifted letter to shifted letters list

cipher = dict(list(zip(letters, shifted_letters)))                  # Defining the cipher

cipher_word = ''                                                    # Empty string to build the cipher word
for letter in word:                                                 # For each letter in this word
    cipher_word += cipher[letter]                                   # Adding the ciphered letters to build the word

print(cipher_word)                                                  # Printing the ciphered word.
;