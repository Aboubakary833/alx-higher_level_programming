#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    _values = sorted(a_dictionary.values())
    for el in a_dictionary:
        if a_dictionary[el] == _values[-1]:
            return el
