#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    _keys = list(a_dictionary)
    if (key in _keys):
        del a_dictionary[key]
    return a_dictionary
