"""The insertion sort algorithm."""


def isort(xs: list[int]) -> None:
    i: int = 1 # i is progress
    j: int # j is circled item (current item index to cprrectly place/sort)
    while i < len(xs):
        j = 1 # swapping back incorrect items
        while j > 0 and xs[j] < xs[j - 1]: # ^^
            swap(xs, j, j - 1) # ^^
            j -= 1 # ^^

        i += 1


def swap(xs: list[int], i: int, j: int) -> None:
    temp: int = xs[i]
    xs[i] = xs[j]
    xs[j] = temp


nums: list[int] = [2, 3, 1, 4]
isort(nums)
print(nums)