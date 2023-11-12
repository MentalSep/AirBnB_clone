#!/usr/bin/python3
""" Unittest for Review class """
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """ Test cases for Review class """
    def setUp(self):
        """ Create instance global  """
        self.review = Review()

    def tearDown(self):
        """ Clean All test case """
        del self.review

    def test_instance(self):
        """ Test Case to check instance """
        self.assertIsInstance(self.review, Review)
        self.assertIsInstance(self.review, BaseModel)

    def test_attributes(self):
        """ Test Case to check attributes """
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))
