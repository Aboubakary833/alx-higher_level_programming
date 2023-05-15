#!/usr/bin/python3

def no_c(my_string):
    if (isinstance(my_string, str)):
        return my_string.replace('C', '').replace('c', '')
