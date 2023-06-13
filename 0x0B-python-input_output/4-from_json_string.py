#!/usr/bin/python3

"""Parse a json string"""

import json


def from_json_string(my_str):
    """from_json_string

    Args:
            my_str (str): Json string to parse
    """
    return json.loads(my_str)
