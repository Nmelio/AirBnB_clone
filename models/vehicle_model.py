#!/usr/bin/python3
"""This file contains the implementation of the vehicle class."""


class Vehicle:
    """A class representing a vehicle."""

    def __init__(self, num_of_tires=4, brand="Toyota"):
        """
            Class Initialiser.

        Args:
            num_of_tires (_type_): _description_
        """
        self.num_of_tires = num_of_tires
        self.brand = brand

    @property
    def num_of_tires(self):
        """Number of tires getter.

        Returns:
            _type_: _description_
        """
        return self.__num_of_tires

    @num_of_tires.setter
    def num_of_tires(self, value):
        """num_of_tires setter.

        Args:
            value (int): Value of number of tires

        Raises:
            TypeError: num_of_tires must be an integer
            ValueError: num_of_tires must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("num_of_tires must be an integer")
        if value < 0:
            raise ValueError("num_of_tires must be >= 0")
        self.__num_of_tires = value

    @property
    def brand(self):
        """Brand Getter.

        Returns:
            String: name of the brand of current vehicle
        """
        return self.__brand

    @brand.setter
    def brand(self, value):
        """Brand Setter.

        Args:
            value (str): Name of brand

        Raises:
            TypeError: brand is not of type string
        """
        if not isinstance(value, str):
            raise TypeError("brand is not of type string")
        self.__brand = value
