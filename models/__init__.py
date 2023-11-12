#!/usr/bin/env python3
""" Module to create unique FileStorage instance for the application """
from models.engine.file_storage import FileStorage

""" Create a unique FileStorage instance for the application"""
storage = FileStorage()
storage.reload()
