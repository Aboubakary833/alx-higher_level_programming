#!/usr/bin/python3

"""Student to json module"""


class Student:
    """Student class
    """

    def __init__(self, first_name, last_name, age):
        """__init__: Initialize a new student

        Args:
                first_name (str): Student firstname
                last_name (str): Student lastname
                age (int): Student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to_json

             Args:
                     attrs (any, None): Attributes. Defaults to None.
             Returns:
                     dict: Dictionary representation of the instance
             """
        if attrs and all(type(attr) == str for attr in attrs):
            return {
                k: self.__dict__[k]
                for k in attrs
                if attrs and self.__dict__.get(k)
            }
        else:
            return self.__dict__
