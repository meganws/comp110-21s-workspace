"""Examples of list and loop algorithms."""

def sum_algo(xs: list[int]) -> int:
    """Summation of input list is returned."""
    total: int = 0
    i: int = 0
    while i < len(xs):
        total += xs[i]
        i += 1

    return total


single: list[int] = [110]
many: list[int] = [1, 3, 5]
print(sum_algo(single))
print(sum_algo(many))