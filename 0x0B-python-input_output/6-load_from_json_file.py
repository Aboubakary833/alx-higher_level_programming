#!/usr/bin/python3

"""Read from a json file"""

import json


def load_from_json_file(filename):
    """load_from_json_file

    Args:
            filename (str): Json file to read from
    """
    with open(filename, 'r') as file:
        return json.load(file)
