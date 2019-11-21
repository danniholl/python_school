# Python Assignment 6
# Roy Crippen
# ENG 101
# Due 11/20/2019

# The goal of this code is to define two functions. The first function receives either a list or a single item from
# the user and computes the total cost of that single item or list of items. It also will update the amount of stock
# related to those items. The second function checks the store stock and prints out the items that need to be restocked.

# Here are the two dictionaries that will be used. They could be combined into one dictionary, but I'll leave them as
# they were given to me.
stock = {
    "tomato soup": 20,
    "cheese": 10,
    "bread": 3,
    "milk": 1,
    "butter": 7,
    "coffee": 8,
    "ice cream": 5,
    "orange juice": 12,
    "bacon": 5,
    "tortilla chips": 4,
    "ramen": 20
}
prices = {
    "tomato soup": 1.85,
    "cheese": 3.99,
    "bread": 2.50,
    "milk": 3.59,
    "butter": 1.99,
    "coffee": 5.99,
    "ice cream": 2.99,
    "orange juice": 2.50,
    "bacon": 5.49,
    "tortilla chips": 3.99,
    "ramen": 0.99
}


# Here I define the grocery_cost function. It receives either a list or a single item from the user first. Then it
# immediately checks if it was given a list or not. If it was not given a list it converts the single item into a
# list. Then it initializes a running total and checks if the each item in the list is misspelled. If the item in the
# list is misspelled it prints out the items not in stock and does not add to the running total. If the user inputs a
# valid, in-stock food item, then the cost gets added to the running total, the stock of that item is reduced by 1
# and it loops back through the next item in the list until the list is complete which it will then print out the total
# cost.
def grocery_cost(food):
    if type(food) is not list:
        food = [food]
    total_cost = 0
    for item in food:
        if item not in stock:
            print('"{}" is not a food we carry.'.format(item))
            continue
        if stock[item] < 1:
            print('We do not have {} in stock.'.format(item))
        else:
            total_cost += prices[item]
            stock[item] -= 1
    print('Your total cost is ${:,.2f}'.format(total_cost))


def stock_check():
    """Here I define the stock_check function. It loops through each food item in the stock dictionary and checks if the
    value is less than 5. If the value is less than 5 I print the food item that needs to be ordered."""
    for key, value in stock.items():
        if value < 5:
            print('You need to order more {}.'.format(key))


# Here are some tests that I ran to check my grocery_cost function.
# grocery_cost(['coffee', 'coffee', 'vice cream', 'bacon'])
# grocery_cost('offee')
# grocery_cost(['coffee', 'coffee', 'coffee', 'coffee', 'coffee', 'coffee', 'coffee', 'coffee', 'coffee'])

# Here I call the functions, you can put a list of items found in the stock dictionary or any single item found in
# the stock dictionary into the grocery_cost function.
grocery_cost('coffee')
stock_check()
