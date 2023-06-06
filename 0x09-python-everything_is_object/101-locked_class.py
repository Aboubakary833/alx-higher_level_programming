#!/usr/bin/python3
"""
Class with no class or object attribute
"""


class LockedClass():
    """
    Prevent user from creating new instance attribute
    dynamically unless attribute is "first_name"
    """

    __slots__ = "first_name"
