#!/usr/bin/python3
"""
    Unittest for Base
"""

import unittest
from models import base
Base = base.Base



class TestBase(unittest.TestCase):
    """
        test for Base
    """
    def test_creation_id(self):
        """
            test if value of id has the good assignment
        """
        base_1 = Base(5)
        base_2 = Base()
        base_3 = Base(-10.2)
        base_4 = Base(3)
        base_5 = Base(None)

        self.assertEqual(base_1.id, 5)
        self.assertEqual(base_2.id, 1)
        self.assertEqual(base_3.id, -10.2)
        self.assertEqual(base_4.id, 3)
        self.assertEqual(base_5.id, 2)

    def test_to_json_string(self):
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, '[]')

    def test_from_json_string(self):
        json_string = Base.from_json_string(None)
        self.assertEqual(json_string, [])


if __name__ == '__main__':
    unittest.main()
