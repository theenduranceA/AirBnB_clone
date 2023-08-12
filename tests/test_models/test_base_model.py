#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import unittest
import inspect
import io
import pep8
from datetime import datetime
import uuid
from contextlib import redirect_stdout
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    class for testing BaseModel class' methods
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class method for the doc tests
        """
        cls.setup = inspect.getmembers(BaseModel, inspect.isfunction)

    def setUp(self):
        """Set up method for object BM of BAseModel"""
        self.BM = BaseModel()

    def tearDown(self):
        """Set tmp object"""
        self.BM = None

    def test_pep8_conformance_BaseModel(self):
        """
        Test that base_model.py file conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_BaseModel(self):
        """
        Test that test_base_model.py file conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/\
                                        test_base_model.py'])
        self.assertEqual(result.total_errors, 1,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """
        Tests if module docstring documentation exist
        """
        self.assertTrue(len(BaseModel.__doc__) >= 1)

<<<<<<< HEAD
    def test_class_docstring(self):
        """
        Tests if class docstring documentation exist
        """
        self.assertTrue(len(BaseModel.__doc__) >= 1)

    def test_func_docstrings(self):
        """
        Tests if methods docstring documntation exist
        """
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)

    def test_type(self):
        """test method for type testing of BaseModel
        """
        self.assertIsInstance(self.BM, BaseModel)
        self.assertEqual(type(self.BM), BaseModel)

    def test_basic_attribute_set(self):
        """test method for basic attribute assignment
        """
        self.BM.first_name = 'Meco'
        self.BM.last_name = 'Montes'
        self.assertEqual(self.BM.first_name, 'Meco')
        self.assertEqual(self.BM.last_name, 'Montes')

    def test_str(self):
        """tests str method
        """
        string = str(self.BM)
        BMid = "[{}] ({}) {}".format(self.BM.__class__.__name__, self.BM.id,
                                     self.BM.__dict__)
        test = BMid in string
        self.assertEqual(True, test)
        test = "updated_at" in string
        self.assertEqual(True, test)
        test = "created_at" in string
        self.assertEqual(True, test)
        test = "datetime" in string
        self.assertEqual(True, test)
=======
class TestBase_Model(unittest.TestCase):
    '''start tests'''

    def test_docstring(self):
        '''test if funcions, methods, classes
        and modules have docstring'''
        msj = "Módulo does not have docstring"
        self.assertIsNotNone(models.base_model.__doc__, msj)  # Modules
        msj = "Class does not have docstring"
        self.assertIsNotNone(BaseModel.__doc__, msj)  # Classes

    def test_executable_file(self):
        '''test if file has permissions u+x to execute'''
        # Check for read access
        is_read_true = os.access('models/base_model.py', os.R_OK)
        self.assertTrue(is_read_true)
        # Check for write access
        is_write_true = os.access('models/base_model.py', os.W_OK)
        self.assertTrue(is_write_true)
        # Check for execution access
        is_exec_true = os.access('models/base_model.py', os.X_OK)
        self.assertTrue(is_exec_true)

    def test_is_an_instance(self):
        '''check if my_model is an instance of BaseModel'''
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)

    def test_id(self):
        '''test if the id of two instances are different'''
        my_model = BaseModel()
        my_model1 = BaseModel()
        self.assertNotEqual(my_model.id, my_model1.id)

    def test_save(self):
        '''check if the attribute updated_at (date) is updated for
        the same object with the current date'''
        my_model2 = BaseModel()
        first_updated = my_model2.updated_at
        my_model2.save()
        second_updated = my_model2.updated_at
        self.assertNotEqual(first_updated, second_updated)
>>>>>>> 385d521018901177965474fba9f8c46acef14d29

    def test_to_dict(self):
        """tests to_dict method
        """
        my_dict = self.BM.to_dict()
        self.assertEqual(str, type(my_dict['created_at']))
        self.assertEqual(my_dict['created_at'],
                         self.BM.created_at.isoformat())
        self.assertEqual(datetime, type(self.BM.created_at))
        self.assertEqual(my_dict['__class__'],
                         self.BM.__class__.__name__)
        self.assertEqual(my_dict['id'], self.BM.id)

    def test_to_dict_more(self):
        """tests to_dict method
        """
        my_dict = self.BM.to_dict()
        created_at = my_dict['created_at']
        time = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(self.BM.created_at, time)

    def test_from_dict_basic(self):
        """tests from_dict method
        """
        my_dict = self.BM.to_dict()
        BM1 = BaseModel(**my_dict)
        self.assertEqual(BM1.id, self.BM.id)
        self.assertEqual(BM1.updated_at, self.BM.updated_at)
        self.assertEqual(BM1.created_at, self.BM.created_at)
        self.assertEqual(BM1.__class__.__name__,
                         self.BM.__class__.__name__)

    def test_from_dict_hard(self):
        """test for the from_dict method for BaseModel objects
        """
        self.BM.student = 'Science'
        my_dict = self.BM.to_dict()
        self.assertEqual(my_dict['student'], 'Science')
        BM1 = BaseModel(**my_dict)
        self.assertEqual(BM1.created_at, self.BM.created_at)

    def test_unique_id(self):
        """test for id in BaseModel objects
        """
        BM1 = BaseModel()
        BM2 = BaseModel()
        self.assertNotEqual(self.BM.id, BM1.id)
        self.assertNotEqual(self.BM.id, BM2.id)

    def test_id_type_string(self):
        """test id in BaseModel is a string
        """
        self.assertEqual(type(self.BM.id), str)

    def test_updated_time(self):
        """test that updated time gets updated
        """
        time1 = self.BM.updated_at
        self.BM.save()
        time2 = self.BM.updated_at
        self.assertNotEqual(time1, time2)
        self.assertEqual(type(time1), datetime)
