#!/usr/bin/python3
"""This file contains the implementation of the BaseModel Class."""


import uuid
from datetime import datetime


class BaseModel:
    """Class representing the base model."""

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            nowSnapshot = datetime.now()
            self.id = str(uuid.uuid4())
            self.created_at = nowSnapshot
            self.updated_at = nowSnapshot

    def __str__(self):
        s = "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
        return s

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dict_snapshot = self.__dict__.copy()
        dict_snapshot['__class__'] = self.__class__.__name__
        dict_snapshot['created_at'] = self.created_at.isoformat()
        dict_snapshot['updated_at'] = self.updated_at.isoformat()
        return dict_snapshot
        
