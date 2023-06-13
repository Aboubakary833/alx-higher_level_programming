#!/usr/bin/python3

"""Stringify a class."""


def class_to_json(obj):
    """class_to_json

    Args:
        obj (str): Object which class to serialize

    Returns:
        dict: dictionary description
    """
    return obj.__dict__
