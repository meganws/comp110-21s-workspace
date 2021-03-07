"""Some examples of lists concepts."""

rolls: list[int] # declare a variable whose type is a list of integers

rolls = [2, 3, 2, 6] # initializr with list literal syntax

print(f"Length of rolls is {len(rolls)}")
print(f"The last value in the list is {rolls[len(rolls) - 1]}")
from random import randint
rolls.append(randint(1, 6)) # list's append method adds an item to the end of the list
print(rolls)

rolls.pop() # list's pop method, with no argument, removes the last item of the list
rolls.pop(0) #list's pop method, with one argument, pops a specific index
print(rolls)


words: list[str] = list() # construct an empty list using the list contructor
words.append("Hello")
print(words)