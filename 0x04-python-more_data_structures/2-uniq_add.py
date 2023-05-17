#!/usr/bin/python3

def uniq_add(my_list=[]):
    total = 0
    for el in set(my_list):
        total += el
    return total
