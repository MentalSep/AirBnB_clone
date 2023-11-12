#!/usr/bin/python3
""" Unittest for Review class """
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """ Test cases for Review class """

    def test_docstring(self):
        """ checks for docstrings """
        self.assertIsNotNone(Review.__doc__)

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

    def test_str(self):
        """ Test Case to check __str__ method """
        string = "[Review] ({}) {}".format(self.review.id, self.review.__dict__)
        self.assertEqual(string, str(self.review))
