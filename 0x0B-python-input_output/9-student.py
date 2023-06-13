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

    def to_json(self):
        """Stringify current student"""
        return self.__dict__
