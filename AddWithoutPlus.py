def AddWithoutPlus(n: int, m: int) -> int:
    while m != 0:
        sum = n ^ m
        carry = (n & m) << 1
        n = sum
        m = carry
    return n


if __name__ == "__main__":
    print(AddWithoutPlus(3, 5))
