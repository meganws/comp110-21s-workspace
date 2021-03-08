"""EX03 - palindromify function."""

__author__: str = "730388741"


def main() -> None:
    """Entrypoint of the program."""
    print(palindromify("race", False))
    print(palindromify("han", True))
    print(palindromify("red", True))
    print(palindromify("live on time ", False))
    return None


def palindromify(word: str, true_false: bool) -> str:
    """Making or finding the palindrome."""
    if true_false == True:
        result = reverse_even(word)
    else:
        result = reverse_odd(word)
    return result


def reverse_even(word: str) -> str:
    """Palindroming word with even number of characters."""
    str1 = ''
    for character in word:
        str1 = character + str1     
    word += str1
    return word


def reverse_odd(word: str) -> str:
    """Palindroming word with odd number of characters."""
    str1 = ''
    word_length = len(word) - 1
    while word_length >= 0:
        str1 += word[word_length]
        word_length -= 1
    word += str1
    return word


if __name__ == "__main__":
    main()
