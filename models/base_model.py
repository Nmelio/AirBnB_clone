#!/usr/bin/python3
"""This file contains the implementation of the BaseModel Class."""

import models
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """
    Base Model Class.

    Attributes:
        id (str): A unique identifier for the instance.
        created_at (datetime): Created timestamp.
        updated_at (datetime): Updated timestamp.

    Methods:
        __init__(*args, **kwargs): Initializes instance attributes.
        __str__(): Returns a string representation of the instance.
        save(): Updates the `updated_at` timestamp and saves changes.
        to_dict(): Returns a dictionary representation of the
                    instance'sattributes.

    """

    def __init__(self, *args, **kwargs):
        """
        Initialize instance attributes.

        Args:
            *args: Additional positional arguments (ignored).
            **kwargs: Keyword arguments used to populate instance attributes.

        Attributes 'created_at' and 'updated_at' are formatted as datetime.
        """
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
        """
        Return a string representation of the instance.

        Returns:
            str: A formatted string containing
                    the class name, ID, and attribute dictionary.
        """
        s_rep = "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)
        return s_rep

    def save(self):
        """
        Update the `updated_at` attribute and save changes.

        This method updates the `updated_at` attribute with
        the current datetime and saves the changes to the storage.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Convert the instance's attributes to a dictionary.

        Returns:
            dict: A dictionary containing all attributes of the instance.

        The 'created_at' and 'updated_at' attributes are formatted
        as ISO 8601 strings.
        """
        dict_snapshot = self.__dict__.copy()
        dict_snapshot['__class__'] = self.__class__.__name__
        dict_snapshot['created_at'] = self.created_at.isoformat()
        dict_snapshot['updated_at'] = self.updated_at.isoformat()
        return dict_snapshot
