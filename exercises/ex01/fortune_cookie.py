"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730388741"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


print("Your fortune cookie says...")
number = randint(1, 4)
if number >= 3:
    if number == 3:
        print("A beautiful soul will enter your life soon")
    else:
        print("Sit down and enjoy the world")
else:
    if number == 2:
        print("Don't put off what you can do today, tomorrow")
    else:
        print("Do or do not, there is no try")
print("Now, go spread positive vibes!")