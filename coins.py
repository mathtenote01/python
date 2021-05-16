def ways_of_represent(num: int) -> int:
    return ways_of_representhelp(num, 1)


def ways_of_representhelp(num: int, count):
    if num == 1:
        return count
    if num % 25 == 0:
        return ways_of_representhelp(num - 1, count + 3)
    elif num % 10 == 0:
        return ways_of_representhelp(num - 1, count + 2)
    elif num % 5 == 0:
        return ways_of_representhelp(num - 1, count + 1)
    else:
        return ways_of_representhelp(num - 1, count)


if __name__ == "__main__":
    print(ways_of_represent(500))
