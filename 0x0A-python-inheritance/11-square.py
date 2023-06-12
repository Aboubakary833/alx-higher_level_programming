#!/usr/bin/python3
"""Square extending Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """quare extending Rectangle."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the Square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
