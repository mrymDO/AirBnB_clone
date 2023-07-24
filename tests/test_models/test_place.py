#!/usr/bin/python3
"""Unittest for place module"""

from models.base_model import BaseModel
from models.place import Place
import pycodestyle
import unittest
import inspect
import os


class TestPlace(unittest.TestCase):
    """tests for place class"""

    def test_place_docstring(self):
        """test docstring"""
        place = Place()
        module_docstring = inspect.getdoc(place)
        self.assertTrue(len(module_docstring) >= 1)

        class_docstring = inspect.getdoc(Place)
        self.assertTrue(len(class_docstring) >= 1)

    def test_place_pycodestyle(self):
        """test pycodestyle place module and test_place"""
        style = pycodestyle.StyleGuide()
        result = style.check_files(['models/place.py'])
        self.assertEqual(
                result.total_errors, 0, "Found style errors or warnings.")

        style2 = pycodestyle.StyleGuide()
        result2 = style2.check_files(['tests/test_models/test_place.py'])
        self.assertEqual(
                result2.total_errors, 0, "Found style errors or warnings.")

    def test_file(self):
        """test if place module is executable"""
        file_path = 'models/place.py'
        self.assertTrue(os.access(file_path, os.X_OK))
        self.assertTrue(os.access(file_path, os.R_OK))
        self.assertTrue(os.access(file_path, os.W_OK))

    def test_place(self):
        """Test Place Class"""
        self.assertTrue(issubclass(Place, BaseModel))
        place = Place()
        place2 = Place()
        attributes = ['id', 'created_at', 'updated_at', 'city_id', 'user_id',
                      'name', 'description', 'number_rooms',
                      'number_bathrooms', 'max_guest', 'price_by_night',
                      'latitude', 'longitude', 'amenity_ids']

        for attribute in attributes:
            self.assertTrue(hasattr(place, attribute))

        self.assertNotEqual(place, place2)

    def test_place_save(self):
        """test save method"""
        place = Place()
        place_update = place.updated_at
        place.save()
        self.assertIsNotNone(place.updated_at)
        self.assertNotEqual(place_update, place.updated_at)

    def test_place_to_dict(self):
        """test to_dict()"""
        place = Place()
        place_dict = place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertIsInstance(place_dict['created_at'], str)
        self.assertIsInstance(place_dict['updated_at'], str)

    def test_place_str(self):
        """test the __str__() method of place class"""
        place = Place()
        place_str = str(place)
        self.assertEqual(place_str, "[Place] ({}) {}".format(
            place.id, place.__dict__))


if __name__ == "__main__":
    unittest.main()
