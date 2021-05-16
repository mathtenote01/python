def multiply(n: int, m: int):
    if n < m:
        bigger = m
        smaller = n
    else:
        bigger = n
        smaller = m
        return multiplyHelper(smaller, bigger)


def multiplyHelper(smaller: int, bigger: int):
    if smaller == 0:
        return 0
    elif smaller == 1:
        return bigger

    s = int(smaller // 2)
    halfProd = int(multiplyHelper(s, bigger))
    if smaller % 2 == 0:
        return halfProd + halfProd
    else:
        return halfProd + halfProd + bigger


if __name__ == "__main__":
    print(multiply(18975, 13965))
