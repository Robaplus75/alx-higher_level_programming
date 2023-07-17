#!/usr/bin/python3
from models.square import Square
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
import os
import sys
import json
import unittest
"""Module for unitest of base class."""


class TestBase(unittest.TestCase):
    """
    test for classes
    """
    def setUp(self):
        """
        for redirecting stdout
        """
        sys.stdout = StringIO()

    def tearDown(self):
        """
        removes everything
        """
        sys.stdout = sys.__stdout__

    def test_docstrings(self):
        self.assertIsNotNone(Base.__doc__)
        self.assertIs(hasattr(Base, "__init__"), True)
        self.assertIsNotNone(Base.__init__.__doc__)

        self.assertIsNotNone(Base.create.__doc__)
        self.assertIs(hasattr(Base, "to_json_string"), True)

        self.assertIsNotNone(Base.from_json_string.__doc__)
        self.assertIs(hasattr(Base, "save_to_file"), True)
        self.assertIsNotNone(Base.save_to_file.__doc__)
        self.assertIs(hasattr(Base, "load_from_file"), True)
        self.assertIsNotNone(Base.load_from_file.__doc__)

        self.assertIs(hasattr(Base, "create"), True)
        self.assertIsNotNone(Base.to_json_string.__doc__)
        self.assertIs(hasattr(Base, "from_json_string"), True)

    def test_id(self):
        """
        checking or obj.id
        """
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        b4 = Base(18)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b4.id, 18)

    def test_from_json_string(self):
        """
        from json string func test
        """
        with self.subTest():
            r1 = Rectangle(10, 7, 2, 8, 1)
            r1_dict = r1.to_dictionary()
            json_dict = Base.to_json_string([r1_dict])

            self.assertIs(type(r1_dict), dict)
            self.assertIs(type(json_dict), str)
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_rectangle(self):
        """
        rectangle test
        """
        R1 = Rectangle(7, 8, 9)
        R1_dict = R1.to_dictionary()
        R2 = Rectangle.create(**R1_dict)
        self.assertNotEqual(R1, R2)

    def test_square(self):
        """
        check for square
        """
        S1 = Square(66, 77, 88, 99)
        S1_dict = S1.to_dictionary()
        S2 = Rectangle.create(**S1_dict)
        self.assertNotEqual(S1, S2)

    def test_file_rectangle(self):
        """
        check for file rectangle func
        """
        R1 = Rectangle(23, 24, 25, 16)
        R2 = Rectangle(102, 2)
        lR = [R1, R2]
        Rectangle.save_to_file(lR)
        lR2 = Rectangle.load_from_file()
        self.assertNotEqual(lR, lR2)

    def test_file_square(self):
        """
        check for file square func
        """
        S1 = Square(31)
        S2 = Square(54, 54, 75, 57)
        lS = [S1, S2]
        Square.save_to_file(lS)
        lS2 = Square.load_from_file()
        self.assertNotEqual(lS, lS2)
