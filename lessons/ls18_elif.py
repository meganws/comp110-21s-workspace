"""Example of elif."""

number: int = int(input("Pick a number: "))
answer: int = 50

# This form of nested else-if statement...
if number < answer:
    print("Too low")

else:
    if number > answer:
        print("Too high")
    else:
        print("You got it!!")


# ...is the same as using elif in this way
if number< answer:
    print("Too low")
elif number > answer:
    print("Too high")
else:
    print("You got it!!")

# elif is short for "else-if"