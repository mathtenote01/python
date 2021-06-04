from typing import List
import random


def Shuffle(n: int) -> List[int]:
    int_list = [i for i in range(n)]
    random_list = [0 for i in range(n)]
    for i in range(n):
        if len(int_list) == 0:
            random_list[i] = int_list[0]
        else:
            tmp = random.randrange(0, n - i)
            random_list[i] = int_list[tmp]
            int_list.remove(int_list[tmp])

    return random_list


if __name__ == "__main__":
    print(Shuffle(52))
