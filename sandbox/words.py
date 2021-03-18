import abc


def main() -> None:
    b: list[str] = a
    f(a)
    g()
    print(b[0])


def f(a: list[str]) -> None:
    a[0] = 'p'
    a = ['m', 'j']


def g() -> None:
    global a
    a[1] = 'y'
    a = ['k', 'g']

a: list[str] = ['w', 'u']


if __name__ == "__main__":
    main()