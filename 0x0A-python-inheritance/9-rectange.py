#!/usr/bin/python3
"""Rectangle class that inherits from BaseGeometry class."""


class BaseGeometry:
    """BaseGeometry."""

    def area(self):
        """area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer_validator

        Args:
            name (str): Name.
            value (int): Value.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle extending BaseGeometry class."""

    def __init__(self, width, height):
        """Intialize a new Rectangle.

        Args:
            width (int): The width of the Rectangle.
            height (int): The height of the Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """area"""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
