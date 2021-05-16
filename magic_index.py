from typing import List


def magicSlow(list: List) -> int:
    for i, val in enumerate(list):
        if val == i:
            return i
    return -1


def magicFast_(list: List) -> int:
    return magicFast(list, 0, len(list) - 1)


def magicFast(list: List, start: int, end: int) -> int:
    if end < start:
        return -1
    mid = int((start + end) / 2)
    if list[mid] == mid:
        return mid
    elif list[mid] > mid:
        return magicFast(list, start, mid - 1)
    else:
        return magicFast(list, mid + 1, end)


list = [-1, 0, 2, 4, 9, 10]
print(magicFast_(list))
print(magicSlow(list))
