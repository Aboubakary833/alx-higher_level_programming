#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    _copy = a_dictionary.copy()
    for key, value in _copy.items():
        _copy[key] = value * 2
    return _copy
