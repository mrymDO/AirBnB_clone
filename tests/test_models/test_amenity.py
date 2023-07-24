#!/usr/bin/python3
"""Unittest for amenity module"""

from models.base_model import BaseModel
from models.amenity import Amenity
import pycodestyle
import unittest
import inspect
import os


class TestAmenity(unittest.TestCase):
    """tests for amenity class"""

    def test_amenity_docstring(self):
        """test docstring"""
        amenity = Amenity()
        module_docstring = inspect.getdoc(amenity)
        self.assertTrue(len(module_docstring) >= 1)

        class_docstring = inspect.getdoc(Amenity)
        self.assertTrue(len(class_docstring) >= 1)

    def test_amenity_pycodestyle(self):
        """test pycodestyle amenity module and test_amenity"""
        style = pycodestyle.StyleGuide()
        result = style.check_files(['models/amenity.py'])
        self.assertEqual(
                result.total_errors, 0, "Found style errors or warnings.")

        style2 = pycodestyle.StyleGuide()
        result2 = style2.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(
                result2.total_errors, 0, "Found style errors or warnings.")

    def test_file(self):
        """test if amenity module is executable"""
        file_path = 'models/amenity.py'
        self.assertTrue(os.access(file_path, os.X_OK))
        self.assertTrue(os.access(file_path, os.R_OK))
        self.assertTrue(os.access(file_path, os.W_OK))

    def test_amenity(self):
        """Test Amenity Class"""
        self.assertTrue(issubclass(Amenity, BaseModel))
        amenity = Amenity()
        amenity2 = Amenity()
        attributes = ['id', 'created_at', 'updated_at', 'name']
        for attribute in attributes:
            self.assertTrue(hasattr(amenity, attribute))

        self.assertNotEqual(amenity, amenity2)

    def test_amenity_save(self):
        """test amenity method"""
        amenity = Amenity()
        amenity_update = amenity.updated_at
        amenity.save()
        self.assertIsNotNone(amenity.updated_at)
        self.assertNotEqual(amenity_update, amenity.updated_at)

    def test_amenity_to_dict(self):
        """test to_dict()"""
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertIsInstance(amenity_dict['created_at'], str)
        self.assertIsInstance(amenity_dict['updated_at'], str)

    def test_amenity_str(self):
        """test the __str__() method of amenity class"""
        amenity = Amenity()
        amenity_str = str(amenity)
        self.assertEqual(amenity_str, "[Amenity] ({}) {}".format(
            amenity.id, amenity.__dict__))


if __name__ == "__main__":
    unittest.main()
