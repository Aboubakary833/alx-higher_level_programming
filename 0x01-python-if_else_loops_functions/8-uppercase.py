#!/usr/bin/python3
def uppercase(str):
    upper_str = ""
    for c in str:
        if (ord(c) in range(97, 123)):
            upper_str += chr(ord(c) - 32)
        else:
            upper_str += c
    print("{}".format(upper_str))
