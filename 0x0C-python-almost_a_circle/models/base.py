#!/usr/bin/python3

"""Base class module"""


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize new Base instance

            Args:
                    id (int, None): Instance id. Defaults to None.
            """
        if id:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
