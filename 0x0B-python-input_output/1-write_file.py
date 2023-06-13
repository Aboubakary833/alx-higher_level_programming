#!/usr/bin/python3

"""Write a string to a file"""


def write_file(filename="", text=""):
    """write_file

    Args:
            filename (str, ""): File to write in. Defaults to "".
            text (str, ""): The string to write. Defaults to "".
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
