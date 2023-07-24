#!/usr/bin/python3
"""Unittest for city module"""

from models.base_model import BaseModel
from models.review import Review
import pycodestyle
import unittest
import inspect
import os


class TestReview(unittest.TestCase):
    """tests for review class"""

    def test_review_docstring(self):
        """test docstring"""
        review = Review()
        module_docstring = inspect.getdoc(review)
        self.assertTrue(len(module_docstring) >= 1)

        class_docstring = inspect.getdoc(Review)
        self.assertTrue(len(class_docstring) >= 1)

    def test_review_pycodestyle(self):
        """test pycodestyle review module and test_review"""
        style = pycodestyle.StyleGuide()
        result = style.check_files(['models/review.py'])
        self.assertEqual(
                result.total_errors, 0, "Found style errors or warnings.")

        style2 = pycodestyle.StyleGuide()
        result2 = style2.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(
                result2.total_errors, 0, "Found style errors or warnings.")

    def test_file(self):
        """test if review module is executable"""
        file_path = 'models/review.py'
        self.assertTrue(os.access(file_path, os.X_OK))
        self.assertTrue(os.access(file_path, os.R_OK))
        self.assertTrue(os.access(file_path, os.W_OK))

    def test_review(self):
        """Test Review Class"""
        self.assertTrue(issubclass(Review, BaseModel))
        review = Review()
        review2 = Review()
        attributes = ['id', 'created_at', 'updated_at', 'place_id',
                      'user_id', 'text']
        for attribute in attributes:
            self.assertTrue(hasattr(review, attribute))

        self.assertNotEqual(review, review2)

    def test_review_save(self):
        """test save method"""
        review = Review()
        review_update = review.updated_at
        review.save()
        self.assertIsNotNone(review.updated_at)
        self.assertNotEqual(review_update, review.updated_at)

    def test_review_to_dict(self):
        """test to_dict()"""
        review = Review()
        review_dict = review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertIsInstance(review_dict['created_at'], str)
        self.assertIsInstance(review_dict['updated_at'], str)

    def test_review_str(self):
        """test the __str__() method of review class"""
        review = Review()
        review_str = str(review)
        self.assertEqual(review_str, "[Review] ({}) {}".format(
            review.id, review.__dict__))


if __name__ == "__main__":
    unittest.main()
