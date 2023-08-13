#!/usr/bin/python3
"""This file contains the implementation of the Review Class."""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review Class.

    This class represents a review and inherits attributes
    and methods from the BaseModel class.

    Attributes:
        place_id (str): The ID of the place associated with the review.
        user_id (str): The ID of the user who created the review.
        text (str): The text content of the review.

    Inherits from:
        BaseModel (class): The base model class for common attributes.

    """

    place_id = ""
    user_id = ""
    text = ""
