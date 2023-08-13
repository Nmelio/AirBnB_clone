#!/usr/bin/python3
"""This file contains the implementation of the User Class."""

from models.base_model import BaseModel


class User(BaseModel):
    """
    User Class.

    This class represents a user and inherits
    attributes and methods from the BaseModel class.

    Attributes:
        email (str): The email address of the user.
        password (str): The password associated with the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.

    Inherits from:
        BaseModel (class): The base model class for common attributes.

    """

    email = ''
    password = ''
    first_name = ''
    last_name = ''
