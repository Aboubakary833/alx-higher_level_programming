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
        if _dict[k] in ['V', 'X'] and k != 0 and _dict[k - 1] == 'I':
            if _dict[k] == 'V':
                equivalent += 4
            elif _dict[k] == 'X':
                equivalent += 8
        else:
            equivalent += romanLetters[_dict[k]]
    return equivalent
