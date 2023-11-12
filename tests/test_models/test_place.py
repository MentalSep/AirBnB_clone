#!/usr/bin/python3
""" UNittest for Place class """
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """ Test cases for Place class """
    def setUp(self):
        """ Create instance """
        self.place = Place()

    def test_inheritance(self):
        """ Test that Place class inherits from BaseModel """
        self.assertIsInstance(self.place, BaseModel)

    def test_attributes(self):
        """ Test that Place class has attributes"""
        self.assertTrue("city_id" in self.place.__dir__())
        self.assertTrue("user_id" in self.place.__dir__())
        self.assertTrue("name" in self.place.__dir__())
        self.assertTrue("description" in self.place.__dir__())
        self.assertTrue("number_rooms" in self.place.__dir__())
        self.assertTrue("number_bathrooms" in self.place.__dir__())
        self.assertTrue("max_guest" in self.place.__dir__())
        self.assertTrue("price_by_night" in self.place.__dir__())
        self.assertTrue("latitude" in self.place.__dir__())
        self.assertTrue("longitude" in self.place.__dir__())
        self.assertTrue("amenity_ids" in self.place.__dir__())

    def test_attribute_type(self):
        """ Test that attributes are the correct type """
        self.assertEqual(type(self.place.city_id), str)
        self.assertEqual(type(self.place.user_id), str)
        self.assertEqual(type(self.place.name), str)
        self.assertEqual(type(self.place.description), str)
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertEqual(type(self.place.number_bathrooms), int)
        self.assertEqual(type(self.place.max_guest), int)
        self.assertEqual(type(self.place.price_by_night), int)
        self.assertEqual(type(self.place.latitude), float)
        self.assertEqual(type(self.place.longitude), float)
        self.assertEqual(type(self.place.amenity_ids), list)

    def test_str(self):
        """ Test that the __str__ method returns the correct output """
        string = "[Place] ({}) {}".format(self.place.id, self.place.__dict__)
        self.assertEqual(string, str(self.place))
