#!/usr/bin/python3

"""Square class module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize new Square

            Args:
                size (int): Square size
                x (int, optional): x axis. Defaults to 0.
                y (int, optional): y axis. Defaults to 0.
                id (_type_, optional): Class id. Defaults to None.
            """
        super().__init__(size, size, x, y, id)

    def __str__(self) -> str:
        """Square representation"""
        _repr = "[Square] ({:d}) ".format(self.id)
        _repr += "{:d}/{:d} - ".format(self.x, self.y)
        _repr += "{:d}".format(self.width, self.height)
        return _repr
