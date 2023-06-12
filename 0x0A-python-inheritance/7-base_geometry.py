#!/usr/bin/python3
"""BaseGeometry module"""


class BaseGeometry:
    """BaseGeometry."""

    def area(self):
        """area

                Raises:
                        Exception: area() is not implemented
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
