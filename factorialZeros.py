from typing import List


def zerosOfFactor(num_list: List[int]) -> int:
    two_count = 0
    five_count = 0
    for elm in num_list:
        while elm % 2 == 0:
            two_count += 1
            elm = elm // 2
        while elm % 5 == 0:
            five_count += 1
            elm = elm // 2
    return max(two_count, five_count)


if __name__ == "__main__":
    num_list = [2, 5, 10, 7]
    print(zerosOfFactor(num_list))
