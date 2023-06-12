#!/usr/bin/python3

"""lookup module"""


def lookup(obj):
    """lookup

    Args:
            obj (any): Object to lookup

    Returns:
            list: List of attributes and method of
            a given object
    """
    return dir(obj)
