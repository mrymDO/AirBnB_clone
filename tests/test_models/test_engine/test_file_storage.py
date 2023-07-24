#!/usr/bin/python3

"""Unittest for file_storage module"""

import unittest
import models
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import pycodestyle


class TestFileStorage(unittest.TestCase):
    """Unittest for FileStorage class"""

    def setUp(self):
        """create new instance of FileStorage before each test"""
        self.storage = FileStorage()
        self.storage._FileStorage__objects = {}
        self.storage.class_mapping = {'BaseModel': BaseModel}

    def tearDown(self):
        """Clean up test environment"""

        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_pycodestyle(self):
        """test pycodestyle"""
        style = pycodestyle.StyleGuide()
        result = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0)

    def test_all(self):
        """Test all() method returns FileStorage.__objects attr"""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)
        all_obj = self.storage.all()
        self.assertIn(f"{obj1.__class__.__name__}.{obj1.id}", all_obj)
        self.assertIn(f"{obj2.__class__.__name__}.{obj2.id}", all_obj)
        self.assertEqual(type(all_obj), dict)
        self.assertIs(all_obj, self.storage._FileStorage__objects)

    def test_new(self):
        """Test the new() method"""
        obj = BaseModel()
        self.storage.new(obj)
        self.assertIn(f"{obj.__class__.__name__}.{obj.id}", self.storage.all())

    def test_save(self):
        """Test the save() method"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        self.assertIn(f"{obj.__class__.__name__}.{obj.id}", new_storage.all())

        with open(self.storage._FileStorage__file_path, "r") as f:
            json_data = json.load(f)
            self.assertIn(f"{obj.__class__.__name__}.{obj.id}", json_data)
            self.assertEqual(
                json_data[f"{obj.__class__.__name__}.{obj.id}"], obj.to_dict())

    def test_reload(self):
        """Test reload when the file exists"""
        obj1 = {"__class__": "BaseModel", "id": "1"}
        obj2 = {"__class__": "BaseModel", "id": "2"}
        with open(self.storage._FileStorage__file_path, "w") as f:
            json.dump({"BaseModel.1": obj1, "BaseModel.2": obj2}, f)

        self.storage.reload()

        self.assertIn("BaseModel.1", self.storage.all())
        self.assertIn("BaseModel.2", self.storage.all())
        self.assertEqual(self.storage.all()[
                         "BaseModel.1"].__class__.__name__, "BaseModel")
        self.assertEqual(self.storage.all()[
                         "BaseModel.2"].__class__.__name__, "BaseModel")
        self.assertEqual(self.storage.all()["BaseModel.1"].id, "1")
        self.assertEqual(self.storage.all()["BaseModel.2"].id, "2")

    def test_invalid_json_format(self):
        corrupted_data = "{ invalid json }"
        with open(self.storage._FileStorage__file_path, "w") as f:
            f.write(corrupted_data)
        self.assertRaises(json.decoder.JSONDecodeError, self.storage.reload)

    def test_non_existing_file(self):
        """Test reload() method with non existing file"""
        print(self.storage.all())
        self.storage.reload()
        print(self.storage.all())
        self.assertEqual(len(self.storage.all()), 0)


if __name__ == "__main__":
    unittest.main()
