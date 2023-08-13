#!/usr/bin/python3
"""This file contains the implementation of the State Class."""

from models.base_model import BaseModel


class State(BaseModel):
    """
    State Class.

    This class represents a state and inherits attributes
    and methods from the BaseModel class.

    Attributes:
        name (str): The name of the state.

    Inherits from:
        BaseModel (class): The base model class for common attributes.

    """

    name = ''
