#!/usr/bin/python3
""" unittest """
import unittest
from models.rectangle import Rectangle
from models.base import Base

from io import StringIO
from contextlib import redirect_stdout


class Test_Rectangle(unittest.TestCase):
    """ unittest """
    def test_init(self):
        r = Rectangle(8, 6, 4, 2, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 8)
        self.assertEqual(r.height, 6)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.area(), 48)

        r  = Rectangle(8, 6)
        self.assertEqual(r.width, 8)
        self.assertEqual(r.height, 6)

        self.assertRaisesRegex(
        TypeError, "width must be an integer", Rectangle, "8", 6, 4, 2, 10)
        self.assertRaisesRegex(
        TypeError, "height must be an integer", Rectangle, 8, "6", 4, 2, 10)
        self.assertRaisesRegex(
        TypeError, "x must be an integer", Rectangle, 8, 6, "4", 2, 10)
        self.assertRaisesRegex(
        TypeError, "y must be an integer", Rectangle, 8, 6, 4, "2", 10)
        self.assertRaisesRegex(
        ValueError, "width must be > 0", Rectangle, -1, 6, 4, 2, 10)
        self.assertRaisesRegex(
        ValueError, "height must be > 0", Rectangle, 8, -1, 4, 2, 10)
        self.assertRaisesRegex(
        ValueError, "x must be >= 0", Rectangle, 8, 6, -1, 2, 10)
        self.assertRaisesRegex(
        ValueError, "y must be >= 0", Rectangle, 8, 6, 1, -2, 10)
        self.assertRaisesRegex(TypeError, "", Rectangle, )
        self.assertRaisesRegex(
        ValueError, "width must be > 0", Rectangle, 0, 6, 4, 2, 10)
        self.assertRaisesRegex(
        ValueError, "height must be > 0", Rectangle, 8, 0, 4, 2, 10)
        
        r1 = Rectangle(3, 2)
        expected_output = '###\n###\n'
        with StringIO() as buffer, redirect_stdout(buffer):
            r1.display()
            result = buffer.getvalue()
        self.assertEqual(result, expected_output)

        r = Rectangle(1, 2, 3, 4)
        r.update(89)
        self.assertEqual(r.id, 89)
        r.update(89, 3)
        self.assertEqual(r.width, 3)

        r = Rectangle(14, 16, 12, 15, 25)
        self.assertEqual(str(r), "[Rectangle] (25) 12/15 - 14/16")
