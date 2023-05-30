#!/usr/bin/python3
"""Define an empty class Square."""


class Square:
    """Square class
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new instance of Square

        Args:
        size: The size of the new Square object
        position: The Square object position
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif (not isinstance(position, tuple) or
                len(position) != 2 or
                not all(isinstance(el, int) for el in position) or
                not all(el >= 0 for el in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__size = size
            self.__position = position

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
        elif (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__size = value

    def my_print(self):
        """Print a Square instance
        """
        if (self.__size == 0):
            print("")
        else:
            [print("") for i in range(0, self.__position[1])]
            for i in range(0, self.__size):
                for j in range(0, self.__position[0]):
                    print(" ", end="")
                for k in range(0, self.__size):
                    print("#", end="")
                print("")

    @property
    def position(self) -> tuple:
        return self.__position

    @position.setter
    def position(self, value):
        """Set a Square instance position
        Args:
        value: Position value
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
