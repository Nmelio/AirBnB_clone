#!/usr/bin/env python3
"""
Unittest implementation for Place class
"""

import unittest
from models.place import Place
import models.place


class TestPlace(unittest.TestCase):
    """ This class test the ``Place`` class"""
    def test_module_doc(self):
        """ Test that a module documentaion exists"""
        self.assertIsNotNone(models.place.__doc__)

    def test_class_doc(self):
        """ Test that ``Place`` class documentaion exists"""
        self.assertIsNotNone(Place.__doc__)

    def test_attribute_city_id(self):
        """ Test with city id"""
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        self.assertEqual(place.city_id, "")
        self.assertTrue(type(place.city_id) == str)

    def test_attribute_user_id(self):
        """ Test with user id"""
        place = Place()
        self.assertTrue(hasattr(place, "user_id"))
        self.assertEqual(place.user_id, "")
        self.assertTrue(type(place.user_id) == str)

    def test_attribute_name(self):
        """ Test with name"""
        place = Place()
        self.assertTrue(hasattr(place, "name"))
        self.assertEqual(place.name, "")
        self.assertTrue(type(place.name) == str)

    def test_attribute_description(self):
        """ Test with description"""
        place = Place()
        self.assertTrue(hasattr(place, "description"))
        self.assertEqual(place.description, "")
        self.assertTrue(type(place.description) == str)

    def test_attribute_number_rooms(self):
        """ Test with number of rooms"""
        place = Place()
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertEqual(place.number_rooms, 0)
        self.assertTrue(type(place.number_rooms) == int)

    def test_attribute_number_bathrooms(self):
        """ Test with number of bathrooms"""
        place = Place()
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertEqual(place.number_bathrooms, 0)
        self.assertTrue(type(place.number_bathrooms) == int)

    def test_attribute_max_guest(self):
        """ Test with max guest"""
        place = Place()
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertEqual(place.max_guest, 0)
        self.assertTrue(type(place.max_guest) == int)

    def test_attribute_price_by_night(self):
        """Test with adding night price"""
        place = Place()
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertEqual(place.price_by_night, 0)
        self.assertTrue(type(place.price_by_night) == int)

    def test_attribute_latitude(self):
        """ Test with adding latitude"""
        place = Place()
        self.assertTrue(hasattr(place, "latitude"))
        self.assertEqual(place.latitude, 0.0)
        self.assertTrue(type(place.latitude) == float)

    def test_attribute_longitude(self):
        """ Test with adding longitude"""
        place = Place()
        self.assertTrue(hasattr(place, "longitude"))
        self.assertEqual(place.longitude, 0.0)
        self.assertTrue(type(place.longitude) == float)

    def test_attribute_amenity_ids(self):
        """ Test with adding amenity id"""
        place = Place()
        self.assertTrue(hasattr(place, "amenity_ids"))
        self.assertEqual(place.amenity_ids, [])
        self.assertTrue(type(place.amenity_ids) == list)


if __name__ == "__main__":
    unittest.main()
