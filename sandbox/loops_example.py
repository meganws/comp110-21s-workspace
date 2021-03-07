"""Examples using loops."""

count: int = 0
while input("Do you need more love? yes/no - ") == "yes":
    # body block of the while loops is evaluated
    # when the test expression is true
    print("I love you!")
    count += 1
    print(f"Count is {count}")

# iterating a specific number of times
i: int = 0 # i is typically short for index
iterations: int = 1000000

while i < iterations:
    if i % 1000 == 0:
        print(f"I love you! i: {i}")
    i += 1 # important that this incriment is NOT in the if statement

print("Have a lovely day.")
