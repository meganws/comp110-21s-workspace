"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730388741"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(fortune_cookie())
    print("Now, go spread positive vibes!")
    return None


def fortune_cookie() -> str:
    """Assigning possible values for fortune."""
    number: int = randint(1, 4)
    if number >= 3:
        if number == 3:
            fortune: str = str("A beautiful soul will enter your life soon")
        else:
            fortune: str = str("Sit down and enjoy the world")
    else:
        if number == 2:
            fortune: str = str("Don't put off what you can do today, tomorrow")
        else:
            fortune: str = str("Do or do not, there is no try")
    return fortune


# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()