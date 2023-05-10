#!/usr/bin/python3
for letter in list(range(97, 123).__reversed__()):
    print("{}".format(chr((letter - 32) if letter % 2 else letter)), end="")
    