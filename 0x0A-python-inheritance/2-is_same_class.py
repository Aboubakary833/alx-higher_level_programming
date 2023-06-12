#!/usr/bin/python3

"""is_same_class module"""


def is_same_class(obj, a_class) -> bool:
    """is_same_class

    Args:
            obj (any): Object
            a_class (any): Class

    Returns:
            bool: True or False
    """
    return type(obj) == a_class
