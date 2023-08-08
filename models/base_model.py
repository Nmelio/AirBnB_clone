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
            self.id = str(uuid.uuid4())
            nowSnapshot = datetime.now()
            self.created_at = nowSnapshot
            self.updated_at = nowSnapshot
