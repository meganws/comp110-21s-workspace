"""Mystery loop function."""

def mystery(xs: list[int]) -> int:
    """???"""
    if len(xs) > 0:
        result: int = xs[0]
        i: int = 1
        while i < len(xs):
            if xs[i] > result:
                result = xs[i]
            i += 1
        return result
    else:
        return -1


empty: list[int] = []
rando: list[int] = [3, 2, 5, 1]
print(mystery(empty))
print(mystery(rando))