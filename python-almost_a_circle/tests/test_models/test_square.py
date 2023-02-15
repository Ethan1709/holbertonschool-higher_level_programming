#!/usr/bin/python3
""" unittest """
import unittest
from models.square import Square
from models.base import Base

from io import StringIO


class Test_Square(unittest.TestCase):
    """ unittest """
    def test_init(self):
        r = Square(8, 4, 2, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.size, 8)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.area(), 64)

        self.assertRaisesRegex(
        TypeError, "width must be an integer", Square, "8", 4, 2, 10)
        self.assertRaisesRegex(
        TypeError, "x must be an integer", Square, 8, "4", 2, 10)
        self.assertRaisesRegex(
        TypeError, "y must be an integer", Square, 8, 4, "2", 10)
        self.assertRaisesRegex(
        ValueError, "width must be > 0", Square, -1, 4, 2, 10)
        self.assertRaisesRegex(
        ValueError, "x must be >= 0", Square, 8, -1, 2, 10)
        self.assertRaisesRegex(
        ValueError, "y must be >= 0", Square, 8, 1, -2, 10)
        self.assertRaisesRegex(TypeError, "", Square, )

        def test_display(self):
            r1 = Square(3, 2)
            expected_output = '###\n###\n'
            with StringIO() as buffer, redirect_stdout(buffer):
                r1.display()
                result = buffer.getvalue()
            self.assertEqual(result, expected_output)

        def test_update(self):
            r = Square(1, 3, 4, 5)
            self.assertEqual(r.update().id, 5)
            self.assertEqual(r.update().width, 1)
            self.assertEqual(r.update().x, 3)
            self.assertEqual(r.update().y, 4)

        def test_str(self):
            r = Square(14, 12, 15, 25)
            self.assertEqual(str(r), "[Rectangle] (25) 12/15 - 14")
