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
        """Get a Square instance area
        Return: int
        """
        return self.__size * self.__size

    @property
    def size(self) -> int:
        """Get a Square instance size
        Return: int"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set a Square instance size
        Args:
        value: The new size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
