#!/usr/bin/python3
"""unittest for class BaseModel"""

import unittest
from models.base_model import BaseModel
import models.base_model as module
from datetime import datetime
from copy import deepcopy


class TestBaseModel(unittest.TestCase):
    """Test BaseModel class"""

    def test_doc_string(self):
        """ Test if doc string exist """
        self.assertNotEqual(module.__doc__, None)
        self.assertNotEqual(BaseModel.__doc__, None)

    def test_attributes(self):
        """Test attributes of BaseModel"""
        my_model = BaseModel()
        my_model2 = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)
        self.assertNotEqual(my_model, my_model2)

    def test_save(self):
        """test save method"""
        my_model = BaseModel()
        previous_updated_at = deepcopy(my_model.updated_at)
        my_model.save()
        self.assertNotEqual(my_model.updated_at, previous_updated_at)

    def test_to_dict(self):
        """test to_dict method"""
        my_model = BaseModel()
        model_dict = my_model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['id'], my_model.id)
        self.assertEqual(
            model_dict['created_at'], my_model.created_at.isoformat())
        self.assertEqual(
            model_dict['updated_at'], my_model.updated_at.isoformat())
        self.assertEqual(model_dict['__class__'], my_model.__class__.__name__)

        self.assertIsInstance(model_dict.get("created_at"), str)
        self.assertIsInstance(model_dict.get("updated_at"), str)

    def test_str(self):
        """test str method"""
        my_model = BaseModel()
        model_str = str(my_model)
        expected_str = "[{}] ({}) {}".format(
            my_model.__class__.__name__, my_model.id, my_model.__dict__)
        self.assertEqual(model_str, expected_str)

    def test_kwarg(self):
        """Create Object from dictionary"""
        my_model = BaseModel()
        model_dict = my_model.to_dict()
        my_new_model = BaseModel(**model_dict)
        self.assertEqual(my_model.id, my_new_model.id)

        self.assertEqual(my_model.created_at, my_new_model.created_at)
        self.assertEqual(my_model.updated_at, my_new_model.updated_at)
        self.assertEqual(
                my_model.__class__.__name__, my_new_model.__class__.__name__)

        self.assertIsInstance(my_new_model, BaseModel)
        self.assertNotEqual(my_model, my_new_model)
        self.assertNotEqual(id(my_model), id(my_new_model))

        self.assertIsInstance(my_new_model.created_at, datetime)
        self.assertIsInstance(my_new_model.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
