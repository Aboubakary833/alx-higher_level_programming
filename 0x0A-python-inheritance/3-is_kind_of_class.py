#!/usr/bin/python3

"""is_kind_of_class module"""


def is_kind_of_class(obj: list, a_class) -> bool:
    """is_kind_of_class

    Args:
            obj (any): Object
            a_class (any): Class

    Returns:
            bool: True or False
    """
    return all(type(obj) == a_class
               or issubclass(type(obj), a_class))
