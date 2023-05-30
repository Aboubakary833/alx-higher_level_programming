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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    def area(self) -> int:
        return self.__size
