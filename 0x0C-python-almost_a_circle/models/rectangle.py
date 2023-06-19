#!/usr/bin/python3

"""Rectange class module
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize new Rectangle

        Args:
                width (int): Rectangle width
                height (int): Rectangle height
                x (int, optional): x axis. Defaults to 0.
                y (int, optional): y axis. Defaults to 0.
                id (_type_, optional): Class id. Defaults to None.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        elif not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        elif not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        elif not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__width = width
            self.__height = height
            self.__x = x
            self.__y = y
            super().__init__(id)

    @property
    def width(self) -> int:
        """Width getter

        Returns:
                int: the width value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Rectange width setter
        Args:
                value (int): The value of the width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self) -> int:
        """Rectangle height getter

        Returns:
                int: Height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Rectange height setter
        Args:
                value (int): The value of the height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self) -> int:
        """x axis position getter

                Returns:
                        int: X axis position value
                """
        return self.__x

    @x.setter
    def x(self, value):
        """Rectange x axis postion setter

                Args:
                        value (int): Rectangle positon at x axis
                """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self) -> int:
        """y axis position getter

                Returns:
                        int: Y axis position value
                """
        return self.__y

    @y.setter
    def y(self, value):
        """Rectange y axis postion setter

                Args:
                        value (int): Rectangle positon at y axis
                """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self) -> int:
        """Return a Rectange area

                Returns:
                        int: Area value
                """
        return (self.__width * self.__height)

    def display(self):
        """Print the rectangle
                """
        for k in range(self.y):
            print()
        for i in range(self.__height):
            for m in range(self.x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self) -> str:
        """Rectangle representation"""
        _repr = "[Rectangle] ({:d}) ".format(self.id)
        _repr += "{:d}/{:d} - ".format(self.x, self.y)
        _repr += "{:d}/{:d}".format(self.width, self.height)
        return _repr

    def update(self, *args, **kwargs):
        """Update an instance of Rectangle
                """
        if args is not None and len(args) is not 0:
            props = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, props[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """A dictionnary representation
        of a Rectangle

                Returns:
                        dict: Representation
                """
        props = ['id', 'width', 'height', 'x', 'y']
        _repr = {}

        for i in props:
            _repr[i] = getattr(self, i)

        return _repr
