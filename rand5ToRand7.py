import random


def rand5ToRand7():
    while True:
        num = 5 * random.randrange(5) + random.randrange(5)
        if num < 21:
            return num & 7


if __name__ == "__main__":
    print(rand5ToRand7())
