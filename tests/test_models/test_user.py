#!/usr/bin/python3
"""Unittest module for User."""

import os
import models
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class Test_User(unittest.TestCase):
    """Class for User test cases."""

    def setUp(self):
        """Set up tests."""
        storage.reset()

    def test_check_user(self):
        """Test to check a user."""
        self.assertEqual(User().__class__.__name__, "User")

    def test_to_dict(self):
        """Tests to dictionary."""
        self.assertTrue(dict, type(User().to_dict()))

    def test_save_with_arg(self):
        u?"""Tests for save."""
        with self.assertRaises(TypeError):
            User().save(None)

    def test_is_an_instance(self):
        """Tests an instance of BaseModel."""
        self.assertIsInstance(User(), User)

    def test_types(self):
        """Test for types."""
        u = User()
        self.assertEqual(type(u.id), str)
        self.assertEqual(type(u.email), str)
        self.assertEqual(type(u.password), str)
        self.assertEqual(type(u.first_name), str)
        self.assertEqual(type(u.last_name), str)
        self.assertEqual(u.created_at.__class__.__name__, "datetime")
        self.assertEqual(u.updated_at.__class__.__name__, "datetime")
