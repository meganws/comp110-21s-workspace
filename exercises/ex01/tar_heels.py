"""An exercise in remainders and boolean logic."""

__author__ = "730388741"


x: int = int(input("Pick a number"))
if int(x) % 2 == 0:
    if x % 7 == 0:
        print("TARHEEL")
    else:
        print("TAR")
else:
    if x % 7 == 0:
        print("HEELS")
    else:
        print("CAROLINA")