#!/usr/bin/python3
"""Unittest for state module"""

from models.base_model import BaseModel
from models.state import State
import pycodestyle
import unittest
import inspect
import os


class TestState(unittest.TestCase):
    """tests for state class"""

    def test_state_docstring(self):
        """test docstring"""
        state = State()
        module_docstring = inspect.getdoc(state)
        self.assertTrue(len(module_docstring) >= 1, "Module's doc")

        class_docstring = inspect.getdoc(State)
        self.assertTrue(len(class_docstring) >= 1, "State class doc")

    def test_state_pycodestyle(self):
        """test pycodestyle state module and test_state"""
        style = pycodestyle.StyleGuide()
        result = style.check_files(['models/state.py'])
        self.assertEqual(
                result.total_errors, 0, "Found style errors or warnings.")

        style2 = pycodestyle.StyleGuide()
        result2 = style2.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(
                result2.total_errors, 0, "Found style errors or warnings.")

    def test_file(self):
        """test if state module is executable"""
        file_path = 'models/state.py'
        self.assertTrue(os.access(file_path, os.X_OK))
        self.assertTrue(os.access(file_path, os.R_OK))
        self.assertTrue(os.access(file_path, os.W_OK))

    def test_state(self):
        """Test State Class"""
        self.assertTrue(issubclass(State, BaseModel))
        state = State()
        state2 = State()
        attributes = ['id', 'created_at', 'updated_at', 'name']
        for attribute in attributes:
            self.assertTrue(hasattr(state, attribute))

        self.assertNotEqual(state, state2)

    def test_state_save(self):
        """test save method"""
        state = State()
        state_update = state.updated_at
        state.save()
        self.assertIsNotNone(state.updated_at)
        self.assertNotEqual(state_update, state.updated_at)

    def test_state_to_dict(self):
        """test to_dict()"""
        state = State()
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertIsInstance(state_dict['created_at'], str)
        self.assertIsInstance(state_dict['updated_at'], str)

    def test_state_str(self):
        """test the __str__() method of state class"""
        state = State()
        state_str = str(state)
        self.assertEqual(state_str, "[State] ({}) {}".format(
            state.id, state.__dict__))


if __name__ == "__main__":
    unittest.main()
