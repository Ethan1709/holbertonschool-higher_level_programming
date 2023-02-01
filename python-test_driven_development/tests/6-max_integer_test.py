#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer
""" Max integer - Unittest """


class TestMaxInteger(unittest.TestCase):
    def test_int(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer(""), None)
    
    def test_value(self):
        self.assertRaises(TypeError, max_integer, ['9', 5])

    def test_float(self):
        self.assertEqual(max_integer([2.2, 3]), 3)
