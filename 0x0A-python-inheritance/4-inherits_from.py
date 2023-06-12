#!/usr/bin/python3
"""inherits_from"""


def inherits_from(obj, a_class):
    """inherits_from

    Args:
        obj (any): Object.
        a_class (type): TClass.
    Returns(bool): True or False
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
