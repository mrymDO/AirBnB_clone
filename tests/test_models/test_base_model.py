#!/usr/bin/python3
"""unittest for class BaseModel"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
from copy import deepcopy


class TestBaseModel(unittest.TestCase):
    """Test BaseModel class"""

    def test_doc_string(self):
        """ Test if doc string exist """
        self.assertNotEqual(BaseModel.__doc__, None)
        self.assertNotEqual(models.base_model.__doc__, None)
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

    def test_str(self):
        """test str method"""
        my_model = BaseModel()
        model_str = str(my_model)
        expected_str = "[{}] ({}) {}".format(
                my_model.__class__.__name__, my_model.id, my_model.__dict__)
        self.assertEqual(model_str, expected_str)


if __name__ == '__main__':
    unittest.main()
