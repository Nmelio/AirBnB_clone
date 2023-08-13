#!/usr/bin/python3
"""This file contains the implementation of the Place Class."""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place Class.

    This class represents a place and inherits
    attributes and methods from the BaseModel class.

    Attributes:
        user_id (str): The ID of the user associated with the place.
        name (str): The name of the place.
        city_id (str): The ID of the city where the place is located.
        description (str): A description of the place.
        number_rooms (int): The number of rooms in the place.
        number_bathrooms (int): The number of bathrooms in the place.
        max_guest (int): The maximum number of guests.
        price_by_night (int): The price per night for renting the place.
        latitude (float): The latitude coordinate of the place's location.
        longitude (float): The longitude coordinate of the place's location.
        amenity_id (str): The ID of the amenity associated with the place.

    Inherits from:
        BaseModel (class): The base model class for common attributes.

    """

    user_id = ""
    name = ""
    city_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
