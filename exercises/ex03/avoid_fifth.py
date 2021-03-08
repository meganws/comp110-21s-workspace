"""EX03 - avoid_fifth function."""

__author__: str = "730388741"


def main() -> None:
    """Entrypoint of the program."""
    print(avoid_fifth("hello"))
    print(avoid_fifth("The sentence we have here possesses E's galore!"))


def avoid_fifth(word: str) -> str:
    """Removing E and e."""
    listing: list[str]
    listing = list(word)
    additions: str = str('')
    for character in listing:
        if character == 'E':
            change: str = str('')
        if character == 'e':
            change: str = str('')
        else:
            if character == 'E':
                change: str = str('')
            else:
                change: str = str(character)
        additions += change
    return additions  


if __name__ == "__main__":
    main()