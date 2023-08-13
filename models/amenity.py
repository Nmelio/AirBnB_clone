#!/usr/bin/python3
"""Implementation of Amenity model."""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity Class.

    Attributes:
        name (str): The name of the amenity.

    Inherits from:
        BaseModel (class): The base model class for common attributes.

    """

    name = ""
