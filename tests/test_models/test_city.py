#!/usr/bin/python3
"""Unittest for city module"""

from models.base_model import BaseModel
from models.city import City
import pycodestyle
import unittest
import inspect
import os


class TestCity(unittest.TestCase):
    """tests for city class"""

    def test_city_docstring(self):
        """test docstring"""
        city = City()
        module_docstring = inspect.getdoc(city)
        self.assertTrue(len(module_docstring) >= 1)

        class_docstring = inspect.getdoc(City)
        self.assertTrue(len(class_docstring) >= 1)

    def test_city_pycodestyle(self):
        """test pycodestyle city module and test_city"""
        style = pycodestyle.StyleGuide()
        result = style.check_files(['models/city.py'])
        self.assertEqual(
                result.total_errors, 0, "Found style errors or warnings.")

        style2 = pycodestyle.StyleGuide()
        result2 = style2.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(
                result2.total_errors, 0, "Found style errors or warnings.")

    def test_file(self):
        """test if city module is executable"""
        file_path = 'models/city.py'
        self.assertTrue(os.access(file_path, os.X_OK))
        self.assertTrue(os.access(file_path, os.R_OK))
        self.assertTrue(os.access(file_path, os.W_OK))

    def test_city(self):
        """Test City Class"""
        self.assertTrue(issubclass(City, BaseModel))
        city = City()
        city2 = City()
        attributes = ['id', 'created_at', 'updated_at', 'name', 'state_id']
        for attribute in attributes:
            self.assertTrue(hasattr(city, attribute))

        self.assertNotEqual(city, city2)

    def test_city_save(self):
        """test save method"""
        city = City()
        city_update = city.updated_at
        city.save()
        self.assertIsNotNone(city.updated_at)
        self.assertNotEqual(city_update, city.updated_at)

    def test_city_to_dict(self):
        """test to_dict()"""
        city = City()
        city_dict = city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertIsInstance(city_dict['created_at'], str)
        self.assertIsInstance(city_dict['updated_at'], str)

    def test_city_str(self):
        """test the __str__() method of city class"""
        city = City()
        city_str = str(city)
        self.assertEqual(city_str, "[City] ({}) {}".format(
            city.id, city.__dict__))


if __name__ == "__main__":
    unittest.main()
