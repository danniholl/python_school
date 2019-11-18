# Python Homework 1 - The Richter Scale
# Roy Crippen
# ENG 101
# Due 11/18/2019

# The goal of this code is to calculate and display the amount of energy in joules and in tons of exploded TNT for
# particular Richter scale values.
from decimal import Decimal

# Setting up the list of richter values
rs = [1.0, 5.0, 9.1, 9.2, 9.5]

# First I calculate the energy in joules and format the output, then I calculate the equivalent amount of energy in
# tons of TNT and format that output as well. Then I print the output.
for r in rs:
    e = '%.5E' % Decimal(10**((1.5*r)+4.8))
    tnt = '%.5E' % Decimal(float(e) / (4.184*10**9))
    print('For Richter value '+str(r)+', the energy released is '+str(e)+' Joules.')
    print('The equivalent energy released in tons of TNT is '+str(tnt)+' tons of tnt.\n')
