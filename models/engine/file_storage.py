#!/usr/bin/python3
"""Store Objects converted to Json"""

from models.base_model import BaseModel
import json


class FileStorage:
    """
    serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    class_mapping = {
        'BaseModel': BaseModel,
    }

    def all(self):
        """return the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        json_dict = {}
        for key, obj in self.__objects.items():
            json_dict[key] = obj.to_dict()
        json_string = json.dumps(json_dict)
        with open(self.__file_path, "w") as f:
            f.write(json_string)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for key, obj_dict in data.items():
                    class_name, obj_id = key.split('.')
                    class_ = self.class_mapping.get(class_name)
                    if class_ is not None:
                        obj = class_(**obj_dict)
                        self.__objects[key] = obj
        except FileNotFoundError:
            pass
