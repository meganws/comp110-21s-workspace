"""Tar Heels exercise redux as a structured program."""

__author__ = "730388741"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    x: int = int(input("Enter an int: "))
    print(tar_heels(x))

def tar_heels(x: int) -> str:
    if int(x) % 2 == 0:
        if x % 7 == 0:
           message: str = str("TAR HEELS")
        else:
           message: str = str("TAR")
    else:
        if int(x) % 7 == 0:
           message: str = str("HEELS")
        else:
           message: str = str("CAROLINA")
    return str(message)

if __name__ == "__main__":
    main()
