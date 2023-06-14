#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0

    dic = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    num = 0

    for a in range(len(roman_string)):
        if dic.get(roman_string[a], 0) == 0:
            return 0

        if (a != (len(roman_string) - 1) and
                dic[roman_string[a]] < dic[roman_string[a + 1]]):
            num += dic[roman_string[a]] * -1
        else:
            num += dic[roman_string[a]]

    return num
