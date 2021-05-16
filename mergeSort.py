from typing import List


def firstIntoSecond(first: List[int], second: List[int]) -> List[int]:
    # result = [0 for i in range(len(first) + len(second))]
    for val in first:
        for i in range(len(second)):
            if i == 0 and second[i + 1] >= val:
                second.insert(i, val)
                break
            if (
                i != 0
                and i != len(second) - 1
                and second[i] <= val
                and second[i + 1] >= val
            ):
                second.insert(i + 1, val)
                break
            if i == len(second) - 1 and second[i] <= val:
                second.insert(i + 1, val)
    return second


if __name__ == "__main__":
    first = [1, 3, 5, 6, 9, 100]
    second = [2, 4, 6, 8, 19]
    result = firstIntoSecond(first, second)
    print(result)
