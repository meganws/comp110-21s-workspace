"""EX03 - prime functions."""

__author__: str = "730388741"


def main() -> None:
    """Entrypoint of the program."""
    print(list_primes(3, 7))
    print(list_primes(10, 20))
    print(list_primes(25, 28))
    print(list_primes(-1, 5))


def is_prime(number: int) -> bool:
    """Checking for prime numbers."""
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                return False
            else:
                i += 1
                return True
    return True


def list_primes(number1: int, number2: int) -> list[int]:
    """Listing prime numbers in a range."""
    results: list[int]
    results = []
    for number in range(number1, number2):
        if number <= number2:
            check = is_prime(number)
            if check is True:
                results.append(number)
    return results


if __name__ == "__main__":
    main()