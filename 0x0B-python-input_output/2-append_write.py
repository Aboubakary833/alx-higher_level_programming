#!/usr/bin/python3

"""Append at the end of a file"""


def append_write(filename="", text=""):
    """append_write

    Args:
            filename (str, ""): File to append to. Defaults to "".
            text (str, ""): The string to append. Defaults to "".
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
