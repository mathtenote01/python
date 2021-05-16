from typing import Tuple


def swapNumber(a: int, b: int) -> Tuple[int, int]:
    a = a - b
    b = b + a
    a = b - a
    return (a, b)


if __name__ == "__main__":
    m = 5
    n = 8
    (m, n) = swapNumber(m, n)
    print(m, n)
