# listクラスを書き換える
from typing import List


def search(list_: List[int], value: int):
    index = 1
    while list_[index] != -1 and list_[index] < value:
        index *= 2
    return binarySearch(list_, value, index // 2, index)


def binarySearch(list_, value, low, high):
    mid = 0

    while low <= high:
        mid = (low + high) // 2
        middle = list_[mid]
        if middle > value or middle == -1:
            high = mid - 1
        elif middle < value:
            low = mid + 1
        else:
            return mid

    return -1

class listAnother(list):

if __name__ == "__main__":
    list_ = [1, 3, 6, 8, 10, 17, 19]
    print(search(list_, 17))
