def multiply(a: int, b: int) -> int:
    result = 0
    if a > 0:
        num = a
        num_ = b
    elif b > 0:
        num = b
        num_ = a
    else:
        a = -a
        b = -b
        num = a
        num_ = b
    for i in range(num):
        result = result + num_
    return result


def minus(a: int, b: int) -> int:
    count = 0
    if a > b:
        while True:
            count += 1
            if count + b == a:
                return count

    else:
        while True:
            count += 1
            if count + a == b:
                return -count


def division(a: int, b: int):
    count = 0
    now = 0
    if a > 0 and b > 0:
        while True:
            now = now + b
            count += 1
            if minus(a, now) < 0:
                return minus(count, 1)

    elif a < 0 and b > 0:
        while True:
            now = minus(now, b)
            count = minus(count, 1)
            if minus(a, now) > 0:
                return count

    elif a > 0 and b < 0:
        while True:
            now = minus(now, b)
            count = minus(count, 1)
            if minus(a, now) < 0:
                return count - 1

    else:
        while True:
            now = now + b
            count = count + 1
            if minus(a, now) > 0:
                return count


if __name__ == "__main__":
    print(multiply(-3, -4))
    print(minus(-14, -7))
    print(division(-19, -3))
