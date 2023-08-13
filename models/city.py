#!/usr/bin/python3
"""This file contains the implementation of the City Class."""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City Class.

    This class represents a city and inherits attributes
    and methods from the BaseModel class.

    Attributes:
        state_id (str): The ID of the state that the city belongs to.
        name (str): The name of the city.

    Inherits from:
        BaseModel (class): The base model class for common attributes.

    """

    state_id = ''
    name = ''
