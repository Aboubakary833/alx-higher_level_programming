#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    _keys = sorted(a_dictionary)
    for key in _keys:
        print("{:s}: {}".format(key, a_dictionary[key]))
