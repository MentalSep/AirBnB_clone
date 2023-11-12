#!/usr/bin/python3
"""unittest module for testing the BaseModel class"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
from time import sleep


class TestBaseModel(unittest.TestCase):
    """Unittest for BaseModel class"""

    def test_docstring(self):
        """Tests for docstrings"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_init(self):
        """Tests for __init__ method"""
        b = BaseModel()
        self.assertTrue(isinstance(b, BaseModel))
        self.assertTrue(hasattr(b, 'id'))
        self.assertTrue(hasattr(b, 'created_at'))
        self.assertTrue(hasattr(b, 'updated_at'))
        self.assertTrue(b.id != "")
        self.assertTrue(b.created_at != "")
        self.assertTrue(b.updated_at != "")
        self.assertTrue(type(b.created_at) is datetime)
        self.assertTrue(type(b.updated_at) is datetime)

        id1 = BaseModel().id
        id2 = BaseModel().id
        self.assertNotEqual(id1, id2)

        t1 = BaseModel()
        sleep(0.05)
        t2 = BaseModel()
        self.assertNotEqual(t1.created_at, t2.created_at)

    def test_str(self):
        """Tests for __str__ method"""
        b = BaseModel()
        string = "[BaseModel] ({}) {}".format(b.id, b.__dict__)
        self.assertEqual(string, str(b))

    def test_save(self):
        """Tests for save method"""
        b = BaseModel()
        old_time = b.updated_at
        b.save()
        self.assertNotEqual(old_time, b.updated_at)

    def test_to_dict(self):
        """Tests for to_dict method"""
        b = BaseModel()
        b_dict = b.to_dict()
        self.assertTrue(type(b_dict) is dict)
        self.assertTrue('to_dict' in dir(b))
        self.assertTrue('__class__' in b_dict)
        self.assertEqual(b_dict['__class__'], 'BaseModel')
        self.assertIsInstance(b_dict['created_at'], str)
        self.assertIsInstance(b_dict['updated_at'], str)

    def test_kwargs(self):
        """Tests for kwargs"""
        b = BaseModel()
        b.name = "alx"
        b.my_number = 1337
        b_dict = b.to_dict()
        b2 = BaseModel(**b_dict)
        self.assertTrue(b is not b2)
        self.assertTrue(type(b2) is BaseModel)
        self.assertEqual(b.id, b2.id)
        self.assertEqual(b.name, b2.name)
        self.assertEqual(b.__dict__, b2.__dict__)
        self.assertEqual(b.created_at, b2.created_at)
        self.assertEqual(b.updated_at, b2.updated_at)
        self.assertEqual(b.my_number, b2.my_number)
