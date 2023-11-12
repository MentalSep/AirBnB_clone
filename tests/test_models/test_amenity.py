#!/usr/bin/python3
""" Unittest for Amenity class """
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """ Test cases for Amenity class """

    def test_docstring(self):
        """ checks for docstrings """
        self.assertIsNotNone(Amenity.__doc__)

    def test_inheritance(self):
        """ checks if Amenity inherits from BaseModel """
        new_amenity = Amenity()
        self.assertIsInstance(new_amenity, BaseModel)

    def test_attributes(self):
        """ checks if Amenity has attributes """
        new_amenity = Amenity()
        self.assertTrue("name" in new_amenity.__dir__())

    def test_type(self):
        """ checks if Amenity.name is class type str """
        new_amenity = Amenity()
        name = getattr(new_amenity, "name")
        self.assertIsInstance(name, str)
