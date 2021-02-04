"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730394883"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


print("Your fortune cookie says...")

if: randint(1, 100) < 30
    print("You will have a good week.")
else: 
    if: randint(1, 100) < 50
        print("You will be productive this month.")
    else:
        if: randint(1, 100) > 50
            print("You will find money soon.")
        else:
            if: randint(1, 100) == 50
                print("You will make a huge discovery soon.")

print("Now, go spread positive vibes!")