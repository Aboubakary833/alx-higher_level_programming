#!/usr/bin/python3

"""MyList module"""


class MyList(list):
    """MyList

    Args:
            list (list): Native list
    """

    def print_sorted(self):
        """print_sorted
        """
        print(sorted(self))
