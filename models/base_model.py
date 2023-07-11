#!usr/bin/python3

"""Base Class Module"""

import uuid
from datetime import datetime
from copy import deepcopy


class BaseModel():
    """ Base model class """

    def __init__(self, *args, **kwargs):
        """Initialize a BaseModel instance"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    self.__setattr__(key,  datetime(value))
                    continue
                self.__setattr__(key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """Update the updated_at attribute with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return a dictionary representation of the instance
        containing all attributes
        """
        new_dict = deepcopy(self.__dict__)
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict['__class__'] = self.__class__.__name__
        return new_dict

    def __str__(self):
        """
        Return a string representation of the instance
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )
