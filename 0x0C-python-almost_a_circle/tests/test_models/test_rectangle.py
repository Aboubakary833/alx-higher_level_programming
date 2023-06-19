#!/usr/bin/python3
"""
    Unittest for Base
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectange(unittest.TestCase):

    """Rectangle test cases"""

    def test_new_rectangle(self):
        """ Test new rectangle """
        first_rectangle = Rectangle(5, 3, 1, 3, 1)
        self.assertEqual(first_rectangle.width, 5)
        self.assertEqual(first_rectangle.height, 3)
        self.assertEqual(first_rectangle.x, 1)
        self.assertEqual(first_rectangle.y, 3)
        self.assertEqual(first_rectangle.id, 1)

        last_rectangle = Rectangle(3, 5)
        self.assertEqual(last_rectangle.width, 3)
        self.assertEqual(last_rectangle.height, 5)
        self.assertEqual(last_rectangle.x, 0)
        self.assertEqual(last_rectangle.y, 0)
        self.assertEqual(last_rectangle.id, 4)

    def test_less_argument(self):
        """ Test less number of args case"""
        with self.assertRaises(TypeError):
            new_rectangle = Rectangle(5)

    def compareTwoRectangle(self):
        """Compare two rectangle instance"""
        first = Rectangle(5, 5)
        second = Rectangle(5, 5)
        self.assertEqual(False, first is second)
        self.assertEqual(False, first.id == second.id)

    def test_is_Base_instance(self):
        """ Test Rectangle is a Base instance """
        new_rectangle = Rectangle(5, 5)
        self.assertEqual(True, isinstance(new_rectangle, Base))


if __name__ == '__main__':
    unittest.main()
