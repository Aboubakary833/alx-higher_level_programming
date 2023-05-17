#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    _list = []
    for _first_el in [el for el in set_1 if el not in set_2]:
        _list.append(_first_el)
    for _second_el in [el for el in set_2 if el not in set_1]:
        _list.append(_second_el)
    return _list
