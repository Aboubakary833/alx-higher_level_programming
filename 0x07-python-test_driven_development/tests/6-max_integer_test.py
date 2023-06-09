#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        orderedList = [1, 2, 3, 4]
        self.assertEqual(max_integer(orderedList), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unorderedList = [1, 2, 4, 3]
        self.assertEqual(max_integer(unorderedList), 4)

    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        beginningWithMax = [7, 4, 3, 2]
        self.assertEqual(max_integer(beginningWithMax), 7)

    def test_empty_list(self):
        """Test an empty list."""
        emptyList = []
        self.assertEqual(max_integer(emptyList), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_element = [9]
        self.assertEqual(max_integer(one_element), 9)

    def test_floats(self):
        """Test a list of floats."""
        floats = [1.5, -4.5, 1.5, 19.7, 5.0]
        self.assertEqual(max_integer(floats), 19.7)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_string(self):
        """Test a string."""
        string = "John"
        self.assertEqual(max_integer(string), 'o')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["A", "list", "of", "string"]
        self.assertEqual(max_integer(strings), "string")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
