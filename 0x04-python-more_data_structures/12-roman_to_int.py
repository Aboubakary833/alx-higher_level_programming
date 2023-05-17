#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    romanLetters = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    equivalent = 0
    _split = [*roman_string]
    _dict = {i: _split[i] for i in range(0, len(_split))}
    for k in _dict:
        if len(_dict) > 1 and _dict[k] == 'X' and _dict[k - 1] == 'I':
            equivalent += 8
        else:
            equivalent += romanLetters[_dict[k]]
    return equivalent
