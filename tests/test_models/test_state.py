#!/usr/bin/python3
""" Unittest for State class """
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """ Test cases for State class """

    def test_docstring(self):
        """ checks for docstrings """
        self.assertIsNotNone(State.__doc__)

    def test_subclass(self):
        """ Test if State inherits from BaseModel """
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_name_attr(self):
        """ Test if State has attribute name, and is empty """
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        s = State()
        new_d = s.to_dict()
        self.assertEqual(type(new_d), dict)
        for attr in s.__dict__:
            self.assertTrue(attr in new_d)
            self.assertTrue("__class__" in new_d)

