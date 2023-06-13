#!/usr/bin/python3

"""Save object stringify result to a file"""

import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file

    Args:
            my_obj (any): Object to serialize
            filename (str): File to save to
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
