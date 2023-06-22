#!/usr/bin/python3
"""test for square.py"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Defines the unit tests for the Square class"""

    def test_init(self):
        """Test the initialization of the Square class"""
        s = Square(5, 1, 2, 3)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 3)

    def test_str(self):
        """Test the __str__ method of the Square class"""
        s = Square(5, 1, 2, 3)
        self.assertEqual(str(s), "[Square] (3) 1/2 - 5")

    def test_size(self):
        """Test the size property and setter of the Square class"""
        s = Square(5, 1, 2, 3)
        self.assertEqual(s.size, 5)
        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)
        with self.assertRaises(TypeError):
            s.size = "10"
        with self.assertRaises(ValueError):
            s.size = -10

    def test_update(self):
        """Test the update method of the Square class"""
        s = Square(5, 1, 2, 3)
        s.update(4, 10, 20, 30)
        self.assertEqual(s.id, 4)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 20)
        self.assertEqual(s.y, 30)

        s.update(id=5, size=15, x=25, y=35)
        self.assertEqual(s.id, 5)
        self.assertEqual(s.size, 15)
        self.assertEqual(s.x, 25)
        self.assertEqual(s.y, 35)

    def test_to_dictionary(self):
        """Test the to_dictionary method of the Square class"""
        s = Square(5, 1, 2, 3)
        d = s.to_dictionary()
        expected = {'id': 3, 'x': 1, 'size': 5, 'y': 2}
        self.assertEqual(d, expected)
