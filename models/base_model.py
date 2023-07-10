#!usr/bin/python3
""" Base Class Module """

import uuid
from datetime import datetime
from copy import deepcopy


class BaseModel():
    """ Base model class """
    
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        new_dict = deepcopy(self.__dict__)
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict['__class__'] = self.__class__.__name__
        return new_dict

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
