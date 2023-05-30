#!/usr/bin/python3
"""Define an empty class Square."""


class Square:
    """Square class
    """
    def __init__(self, size=0):
        """Initialize a new instance of Square

        Args:
        size: The size of the new Square object
        """
        if size <= 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
