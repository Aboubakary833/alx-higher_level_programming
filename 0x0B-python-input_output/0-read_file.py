#!/usr/bin/python3

"""Read file and print it content to stdout"""


def read_file(filename=""):
    """read_file

    Args:
            filename (str, ""): File to read. Defaults to "".
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())
