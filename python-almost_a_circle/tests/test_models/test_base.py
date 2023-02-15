#!/usr/bin/python3
""" unittest """
import unittest
from models.base import Base

from io import StringIO


class Test_Base(unittest.TestCase):
    """ unittest """
    def test_init(self):
        b = Base()
        self.assertEqual(b.id, 1)

        b2 = Base()
        print(b2.id)

        b3 = Base()
        print(b3.id)

        b4 = Base(12)
        print(b4.id)

        b5 = Base()
        print(b5.id)
