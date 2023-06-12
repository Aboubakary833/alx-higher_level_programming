#!/usr/bin/python3

"""MyList module"""


class MyList(list):
    """MyList"""

    def __init__(self):
        """Initialise the MyList"""
        super().__init__()

    def print_sorted(self):
        """print_sorted"""
        sorted_list = sorted(self)
        print(sorted_list)
