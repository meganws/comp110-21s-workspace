def o(x: int) ->int:
        return x * 4


def m(x: int) -> int:
    x = x * 2
    return x


g: int = 3
wow: int = o(m(g))
print(wow)