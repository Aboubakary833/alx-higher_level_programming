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

    @property
    def size(self) -> int:
        """Square size getter
        Returns:
            int: Square size value
        """
        return self.__width

    @size.setter
    def size(self, value):
        """Square size setter
        Raises:
            TypeError: value must be an integer
            ValueError: value must be greater than 0
        Args:
            value (int): Square size value
        """
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        elif value <= 0:
            raise ValueError("value must be > 0")
        else:
            self.__width = value
            self.__height = value

    def update(self, *args, **kwargs):
        """Update a Square instance value
        """
        if args is not None and len(args) is not 0:
            props = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if props[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, props[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)
