#!/usr/bin/python3

import json

"""Stringify to JSON string an object"""


def to_json_string(my_obj):
    """to_json_string

    Args:
            my_obj (any): Object to stringify
    """
    return json.dumps(my_obj)
