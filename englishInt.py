def englishInt(num: int) -> str:
    strFromInt = {
        "0": "",
        "1": "One",
        "2": "Two",
        "3": "Three",
        "4": "Four",
        "5": "Five",
        "6": "Six",
        "7": "Seven",
        "8": "Eight",
        "9": "Nine",
        "10": "Ten",
        "11": "Eleven",
        "12": "Twelve",
        "13": "Thirteen",
        "14": "Fourteen",
        "15": "Fifteen",
        "16": "Sixteen",
        "17": "Seventeen",
        "18": "Eighteen",
        "19": "Nineteen",
        "20": "Twenty",
        "30": "Thirty",
        "40": "Fourty",
        "50": "Fifty",
        "60": "Sixty",
        "70": "Seventy",
        "80": "Eighty",
        "90": "Ninety",
    }
    strFromDigit = {
        "100": "Hundred",
        "1000": "Thousand",
        "1000000": "milion",
    }
    result = ""
    digits = [1000000, 1000, 100]
    for digit in digits:
        if (num // digit) // 1000 != 0 and (
            ((num // digit) // 1000 < 100 and (num // digit) // 1000 > 10)
            or (num // digit) // 1 < 10
        ):
            result += strFromInt[str((num // digit) // 1000 // 10 * 10)]
            result += strFromInt[str((num // digit) // 1000 % 10)]
        elif (num // digit) // 100 != 0 and (
            ((num // digit) // 100 < 100 and (num // digit) // 100 > 10)
            or (num // digit) // 1 < 10
        ):
            result += strFromInt[str((num // digit) // 100 // 10 * 10)]
            result += strFromInt[str((num // digit) // 100 % 10)]
        elif (num // digit) // 10 != 0 and (
            ((num // digit) // 10 < 100 and (num // digit) // 10 > 10)
            or (num // digit) // 1 < 10
        ):
            result += strFromInt[str((num // digit) // 10 // 10 * 10)]
            result += strFromInt[str((num // digit) // 10 % 10)]
        elif (num // digit) // 1 != 0 and (
            ((num // digit) // 1 < 100 and (num // digit) // 1 > 10)
            or (num // digit) // 1 < 10
        ):
            result += strFromInt[str((num // digit) // 1 // 10 * 10)]
            result += strFromInt[str((num // digit) // 1 % 10)]

        if (num // digit) // 1000 + (num // digit) // 100 + (num // digit) // 10 + (
            num // digit
        ) != 0 and digit != 1:
            result += strFromDigit[str(digit)]
        num = num % digit

    result += strFromInt[str(num // 10 * 10)]
    result += strFromInt[str(num % 10)]
    return result


num = 99999999
print(englishInt(num))
