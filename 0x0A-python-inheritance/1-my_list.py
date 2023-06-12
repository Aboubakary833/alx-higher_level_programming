#!/usr/bin/python3

"""MyList module"""


class MyList(list):
    """MyList
    """

    def __init__(self):
        """Initialise the object"""
        super().__init__()

    def print_sorted(self):
        """print_sorted
        """
        print(sorted(self))
