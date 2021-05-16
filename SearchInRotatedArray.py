from typing import List


def SearchInRotatedArray(array: List[int], left: int, right: int) -> int:
    mid = (left + right) // 2
    if right - left < 2:
        return right
    if array[left] > array[mid] and array[mid] < array[right]:
        return SearchInRotatedArray(array, left, mid)
    if array[left] < array[mid] and array[mid] > array[right]:
        return SearchInRotatedArray(array, mid, right)

    return -1


def SearchInRotatedArrayHelp(array):
    return SearchInRotatedArray(array, 0, len(array) - 1)


if __name__ == "__main__":
    array = [11, 14, 17, 19, 25, 30, -4, 1, 3, 6, 9]
    print(SearchInRotatedArrayHelp(array))
