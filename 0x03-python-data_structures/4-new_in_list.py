#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    # Copy of the list
    cpy = my_list[:]
    if (idx < 0 or idx >= list(my_list)):
        return cpy
    else:
        cpy.insert(idx, element)
        cpy.pop(idx + 1)
        return cpy
