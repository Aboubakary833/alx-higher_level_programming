#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    for i in my_list.__reversed__():
        print("{:d}".format(i))
