#!/usr/bin/python3
"""Unittest module for File storage"""

import os
import models
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class Test_FileStorage(Unittest, TestCase):
    """A class for File storage test cases."""

    def setUp(self):
        """simple set up."""
        self.my_model = BaseModel()
        self.storage = FileStorage()

    def tearDown(self):
        """tear down method."""
        if os.path.exists("file.json"):
            os.remove("file.json")
        else:
            pass

    def test_is_an_instance(self):
        '''tests if my_model is an instance of BaseModel'''
        my_model = FileStorage()
        self.assertIsInstance(my_model, FileStorage)

    def test_all(self):
        """tests if all methods returns a dict."""
        self.assertIsInstance(self.storage.all(), dict)

    def test_save(self):
        """tests save method."""
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_new(self):
        """tests new method."""
        self.storage.new(self.my_model)
        new_dict = self.storage.all()
        key = self.my_model.__class__.__name__ + '.' + self.my_model.id
        self.assertIsInstance(new_dict[key], BaseModel)

    def test_reload(self):
        """tests reload."""
        with self.assertRaises(TypeError):
            models.storage.reload(None)

    def test_json_filetype(self):
        """tests if the content of the json file is type dict."""
        self.storage.save()
        self.storage.new(self.my_model)

        with open("file.json", encoding='utf-8') as fd:
            data = json.load(fd)

        self.assertIsInstance(data, dict)

    def test_executable(self):
        """tests for executable permissions."""
        is_read_true = os.access('models/engine/file_storage.py', os.R_OK)
        self.assertTrue(is_read_true)
        is_write_true = os.access('models/engine/file_storage.py', os.W_OK)
        self.assertTrue(is_write_true)
        is_exec_true = os.access('models/engine/file_storage.py', os.X_OK)
        self.assertTrue(is_exec_true)


if __name__ == '__main__':
    unittest.main()
