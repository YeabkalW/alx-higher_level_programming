#!/usr/bin/python3
"""test for base.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test cases for Base class"""

    def test_base_id(self):
        """Test id attribute of Base class"""
        b1 = Base()
        b2 = Base()
        b3 = Base(15)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 15)

    def test_to_json_string(self):
        """Test to_json_string method of Base class"""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        d = {'id': 1, 'width': 2, 'height': 3, 'x': 4, 'y': 5}
        self.assertEqual
        (Base.to_json_string([d]),
         '[{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}]')

    def test_save_to_file(self):
        """Test save_to_file method of Base class"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(
                Base.to_json_string([r1.to_dictionary(), r2.to_dictionary()]),
                file.read()
            )

    def test_from_json_string(self):
        """Test from_json_string method of Base class"""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        s = '[{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}]'
        self.assertEqual(Base.from_json_string(s),
                         [{'id': 1, 'width': 2, 'height': 3, 'x': 4, 'y': 5}])

    def test_create(self):
        """Test create method of Base class"""
        r1_dict = {'id': 1, 'width': 2, 'height': 3, 'x': 4, 'y': 5}
        r1 = Rectangle.create(**r1_dict)
        self.assertEqual(str(r1), "[Rectangle] (1) 4/5 - 2/3")
        r2_dict = {'id': 2, 'size': 3, 'x': 1, 'y': 2}
        r2 = Square.create(**r2_dict)
        self.assertEqual(str(r2), "[Square] (2) 1/2 - 3")

    def test_load_from_file(self):
        """Test load_from_file method of Base class"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        rectangles = Rectangle.load_from_file()
        self.assertEqual(str(rectangles[0]), "[Rectangle] (5) 2/8 - 10/7")
        self.assertEqual(str(rectangles[1]), "[Rectangle] (6) 0/0 - 2/4")
        del r1, r2
