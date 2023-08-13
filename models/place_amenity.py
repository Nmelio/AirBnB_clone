#!/usr/bin/python3
"""This file contains the implementation of the PlaceAmenity Class."""

from models.base_model import BaseModel


class PlaceAmenity(BaseModel):
    """
    PlaceAmenity Class.

    This class represents a relationship between a place and an amenity.
    It inherits attributes and methods from the BaseModel class.

    Attributes:
        place_id (str): The ID of the place associated with the amenity.
        amenity_id (str): The ID of the amenity associated with the place.

    Inherits from:
        BaseModel (class): The base model class for common attributes.
    """

    place_id = ""
    amenity_id = ""
