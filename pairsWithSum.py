from typing import List, Tuple


def pairs_with_sum(num: int, numbers: List[int]) -> List[Tuple[int]]:
    result = []
    removed = numbers.copy()
    for val in numbers:
        if val in removed:
            for _val in numbers:
                if _val in removed:
                    if val + _val == num:
                        result.append((val, _val))
                        if val == _val:
                            removed.remove(val)
                        else:
                            removed.remove(val)
                            removed.remove(_val)
                        break

    return result


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print(pairs_with_sum(6, numbers))
