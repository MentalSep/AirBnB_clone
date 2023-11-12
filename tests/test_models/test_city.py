#!/usr/bin/python3
""" Unittest for City class """
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """ Test cases for City class """

    def test_docstring(self):
        """ checks for docstrings """
        self.assertIsNotNone(City.__doc__)

    def test_inheritance(self):
        """ checks if City inherits from BaseModel """
        new_city = City()
        self.assertIsInstance(new_city, BaseModel)

    def test_attributes(self):
        """ checks if City has attributes """
        new_city = City()
        self.assertTrue("state_id" in new_city.__dir__())
        self.assertTrue("name" in new_city.__dir__())

    def test_type(self):
        """ checks if City.name is class type str """
        new_city = City()
        name = getattr(new_city, "name")
        self.assertIsInstance(name, str)

    def test_str(self):
        """ checks __str__ method """
        new_city = City()
        string = "[City] ({}) {}".format(new_city.id, new_city.__dict__)
        self.assertEqual(string, str(new_city))
