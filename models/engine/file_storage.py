#!/usr/bin/python3
"""Store Objects converted to Json"""

import json

from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity


class FileStorage:
    """
    serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    class_mapping = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

    def all(self):
        """return the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj:
            key = obj.__class__.__name__ + '.' + obj.id
            FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        json_dict = {}
        for key, obj in FileStorage.__objects.items():
            json_dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w", encoding="UTF-8") as f:
            json.dump(json_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        data = {}
        try:
            with open(FileStorage.__file_path, 'r', encoding="UTF-8") as f:
                data = json.load(f)
            for key, obj_dict in data.items():
                class_ = self.class_mapping.get(obj_dict.get("__class__"))
                if class_ != None:
                    obj = class_(**obj_dict)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
