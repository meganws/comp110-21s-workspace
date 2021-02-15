def main() -> None:
    print(please(5))
    return None


def britney(x:int) -> float:
    return x / 2


def please(x: int) -> str:
    f: str = str(free(x))
    b: str = str(britney(x))
    return b + f


def free(x:int) -> int:
    return x + 2


if __name__ == "__main__":
    main()