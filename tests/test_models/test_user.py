#!/usr/bin/python3
""" Unittest for User class """
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """ Unittest for User class """

    def test_docstring(self):
        """Tests for docstrings"""
        self.assertIsNotNone(User.__doc__)

    def test_attributes(self):
        """Tests for attributes"""
        b = User()
        self.assertTrue(hasattr(b, 'email'))
        self.assertTrue(hasattr(b, 'password'))
        self.assertTrue(hasattr(b, 'first_name'))
        self.assertTrue(hasattr(b, 'last_name'))
        self.assertTrue(b.email == "")
        self.assertTrue(b.password == "")
        self.assertTrue(b.first_name == "")
        self.assertTrue(b.last_name == "")
        self.assertTrue(type(b.email) is str)
        self.assertTrue(type(b.password) is str)
        self.assertTrue(type(b.first_name) is str)
        self.assertTrue(type(b.last_name) is str)

    def test_inheritance(self):
        """Tests for inheritance"""
        b = User()
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_str(self):
        """Tests for __str__ method"""
        b = User()
        string = "[User] ({}) {}".format(b.id, b.__dict__)
        self.assertEqual(string, str(b))
