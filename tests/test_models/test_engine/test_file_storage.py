#!/usr/bin/env python3
"""unittest module for testing the FileStorage class"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    """Unitest for FileStorage class"""

    def test_docstring(self):
        """Tests for docstrings"""
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.__init__.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_init(self):
        """Tests for __init__ method"""
        f = FileStorage()
        self.assertTrue(isinstance(f, FileStorage))
        self.assertTrue(hasattr(f, '_FileStorage__file_path'))
        self.assertTrue(hasattr(f, '_FileStorage__objects'))
        self.assertTrue(type(f._FileStorage__file_path) is str)
        self.assertTrue(type(f._FileStorage__objects) is dict)
        self.assertEqual(f._FileStorage__file_path, 'file.json')

    def test_all(self):
        """Tests for all method"""
        f = FileStorage()
        obj_dict = f.all()
        self.assertTrue(type(obj_dict) is dict)
        self.assertEqual(obj_dict, f._FileStorage__objects)

    def test_new(self):
        """Tests for new method"""
        f = FileStorage()
        b = BaseModel()
        f.new(b)
        key = '{}.{}'.format(b.__class__.__name__, b.id)
        self.assertTrue(key in f._FileStorage__objects.keys())
        self.assertTrue(f._FileStorage__objects[key] is b)

    def test_save(self):
        """Tests for save method"""
        f = FileStorage()
        b = BaseModel()
        f.new(b)
        f.save()
        with open('file.json', 'r') as file:
            self.assertTrue(len(file.read()) > 0)

    def test_reload(self):
        """Tests for reload method"""
        f = FileStorage()
        b = BaseModel({id: 11})
        b.save()
        storage.save()
        self.assertEqual(storage.reload(), None)
        f = FileStorage()
        self.assertIsInstance(f.all(), dict)
        f = FileStorage()
        b = BaseModel()
        f.new(b)
        key = '{}.{}'.format(b.__class__.__name__, b.id)
        self.assertEqual(f.all()[key], b)
