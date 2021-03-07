"""for...in loop examples."""

# Iterate through each line of the list
letters: list[str] = ["a", "b", "c", "d", "e", "f", "g"]

# Print each letter in the numbers list
print("Print each letter...")
for letter in letters:
    print(letter)


# print every other letter in letters list
print("Every other letter...")
for i in range(1, len(letters), 2):
    print(letters[i])


# Iterate through each index in a sequence
for i in range(len(letters)):
    print(f"i: {i} - letters[i]: {letters[i]}")