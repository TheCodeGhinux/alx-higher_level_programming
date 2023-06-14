#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
    }
    res = 0
    old_val = 0

    for a in reversed(roman_string):
        val = roman_values[a]

        if val >= old_val:
            res += val
        else:
            res -= val

        old_val = val

    return res
