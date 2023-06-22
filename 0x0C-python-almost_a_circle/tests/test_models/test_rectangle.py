#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    This class contains unit tests for the Rectangle class.
    """

    def setUp(self):
        """
        This method sets up the rectangle instances to be used in the tests.
        """
        self.r1 = Rectangle(5, 10, 2, 1, 1)
        self.r2 = Rectangle(7, 12, id=2)
        self.r3 = Rectangle(3, 6)

    def test_init(self):
        """
        This method tests if the rectangle instance is initialized
        with the correct attributes.
        """
        self.assertEqual(self.r1.width, 5)
        self.assertEqual(self.r1.height, 10)
        self.assertEqual(self.r1.x, 2)
        self.assertEqual(self.r1.y, 1)
        self.assertEqual(self.r1.id, 1)

        self.assertEqual(self.r2.width, 7)
        self.assertEqual(self.r2.height, 12)
        self.assertEqual(self.r2.x, 0)
        self.assertEqual(self.r2.y, 0)
        self.assertEqual(self.r2.id, 2)

        self.assertEqual(self.r3.width, 3)
        self.assertEqual(self.r3.height, 6)
        self.assertEqual(self.r3.x, 0)
        self.assertEqual(self.r3.y, 0)
        self.assertEqual(self.r3.id, 13)

    def test_setters(self):
        """
        This method tests if the rectangle setters raise the correct
        exceptions for invalid values.
        """
        with self.assertRaises(TypeError):
            self.r1.width = 'test'
        with self.assertRaises(ValueError):
            self.r1.width = -1

        with self.assertRaises(TypeError):
            self.r1.height = 'test'
        with self.assertRaises(ValueError):
            self.r1.height = -1

        with self.assertRaises(TypeError):
            self.r1.x = 'test'
        with self.assertRaises(ValueError):
            self.r1.x = -1

        with self.assertRaises(TypeError):
            self.r1.y = 'test'
        with self.assertRaises(ValueError):
            self.r1.y = -1

    def test_area(self):
        """
        This method tests if the area of the rectangle is computed correctly.
        """
        self.assertEqual(self.r1.area(), 50)
        self.assertEqual(self.r2.area(), 84)
        self.assertEqual(self.r3.area(), 18)

    def test_display(self):
        """
        This method tests if the rectangle is displayed correctly.
        """
        expected_output = "\n\n  #####\n  #####\n  #####\n  #####\n  #####\n  \
        #####\n  #####\n  #####\n  #####\n  #####\n"
        self.assertEqual(self.r1.display(), print(expected_output))

    def test_to_dictionary(self):
        """
        This method tests if the rectangle attributes are converted
        to a dictionary correctly.
        """
        expected_output = {'x': 2, 'y': 1, 'id': 1, 'width': 5, 'height': 10}
        self.assertEqual(self.r1.to_dictionary(), expected_output)

    def test_update(self):
        """
        This method tests if the rectangle attributes are updated correctly.
        """
        self.r1.update(5, 7, 14, 3, 2)
        self.assertEqual
