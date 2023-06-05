#!/usr/bin/python3
"""Define an empty class Rectangle."""


class Rectangle:
    """Rectangle class
    number_of_instances - number of Reactange instance
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        elif not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__width = width
            self.__height = height
            __class__.number_of_instances += 1

    @property
    def width(self) -> int:
        """Rectange width getter
                Returns:
                        int: The width of a Rectange
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
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self) -> int:
        """Rectange height getter
                Returns:
                        int: The height of a Rectange
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
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self) -> int:
        """Return a Rectange area

                Returns:
                        int: Area value
                """
        return (self.__width * self.__height)

    def perimeter(self) -> int:
        """Return a Rectange perimeter

        Returns:
            int: Perimeter value
        """
        if (self.__width == 0 or self.__height == 0):
            return 0
        else:
            return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        _repr = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                try:
                    _repr += str(self.print_symbol)
                except Exception:
                    _repr += type(self).print_symbol
            if i < self.__height - 1:
                _repr += "\n"
        return _repr

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        __class__.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if (not isinstance(rect_1, __class__)):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif (not isinstance(rect_2, __class__)):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif (rect_1.area() > rect_1.area()):
            return rect_1
        elif (rect_1.area() < rect_2.area()):
            return rect_2
        else:
            return rect_1

    def square(cls, size=0):
        new = None
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        new = cls(size, size)
        new.__size = size
        return new
