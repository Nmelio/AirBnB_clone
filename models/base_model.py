#!/usr/bin/python3
"""This file contains the implementation of the BaseModel Class."""

import models
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """ defines all common attributes/methods for other classes """

    def __init__(self, *args, **kwargs):
        """ Public instance attributes """
        if kwargs:
            for key, item in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        timestamp_fmt = '%Y-%m-%dT%H:%M:%S.%f'
                        setattr(self, key, datetime.strptime(
                            item, timestamp_fmt))
                    elif key == 'id':
                        setattr(self, key, str(item))
                    else:
                        setattr(self, key, item)

        else:
            now_timestamp = datetime.now()
            self.id = str(uuid4())
            self.created_at = now_timestamp
            self.updated_at = now_timestamp
            models.storage.new(self)

    def __str__(self):
        s_rep = "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)
        return s_rep

    def save(self):
        """ Updates the public instance attribute
        updated_at with the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary containing
        all keys/values of __dict__ of the instance """
        dict_snapshot = self.__dict__.copy()
        dict_snapshot['__class__'] = self.__class__.__name__
        dict_snapshot['created_at'] = self.created_at.isoformat()
        dict_snapshot['updated_at'] = self.updated_at.isoformat()
        return dict_snapshot
