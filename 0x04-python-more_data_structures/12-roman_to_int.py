#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    rs = roman_string
    values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    equivalent = 0
    for i in range(len(rs)):
        if i > 0 and values[rs[i]] > values[rs[i - 1]]:
            equivalent += values[rs[i]] - 2 * values[rs[i - 1]]
        else:
            equivalent += values[rs[i]]
    return equivalent
