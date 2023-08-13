#!/usr/bin/python3
"""Unittest module for File Amenity class"""

import os
import models
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import Amenity


class Test_Amenity(unittest.TestCase):
    """A class for File storage test cases."""

    def setUp(self):
        """Set up test."""
        pass

    def tearDown(self):
        """Test to tear dowm."""
        pass

    def test_save(self):
        """Tests save methods."""
        with self.assertRaises(TypeError):
            Amenity().save(None)

    def test_args(self):
        """Test for correct types in args"""
        a = Amenity()
        self.assertEqual(type(a.id), str)
        self.assertEqual(type(a.name), str)
        self.assertEqual(a.created_at.__class__.__name__, "datetime")
        self.assertEqual(a.updated_at.__class__.__name__, "datetime")

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
