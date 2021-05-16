from typing import List


def power_set(list: List) -> List[List]:
    list_list = []
    print(2 ** (len(list)))
    for i in range(2 ** (len(list))):
        tmp_list = []
        in_or_out = str(bin(i))
        print(in_or_out)
        for j in range(len(list)):
            if j < len(in_or_out):
                if in_or_out[len(in_or_out) - j - 1] == "1":
                    tmp_list.append(list[j])
        list_list.append(tmp_list)
    return list_list


if __name__ == "__main__":
    list = [1, 2, 3, 4, 5, 6]
    print(power_set(list))
