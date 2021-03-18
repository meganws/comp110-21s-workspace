"""Does it loop?"""

def main() -> None:
    print(does_it())

def does_it():
    i = 0
    while i < 10:
        i += 1
        if i == 4:
            return i
    return i


print(main())