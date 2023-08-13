#!/usr/bin/env python3
"""
Unittest implementation for City class
"""
import unittest
from models.city import City
import models.city


class TestCity(unittest.TestCase):
    """Test City class"""

    def test_attribut_state_id(self):
        """ Test with state id"""
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertEqual(city.state_id, "")
        self.assertTrue(type(city.state_id) == str)

    def test_attribut_name(self):
        """ Test with state name"""
        city = City()
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.name, "")
        self.assertTrue(type(city.name) == str)

    def test_class_doc(self):
        """ ``City`` documentation"""
        self.assertIsNotNone(City.__doc__)

    def test_module_doc(self):
        """ Test the city_model module's documentation"""
        self.assertIsNotNone(models.city.__doc__)


if __name__ == "__main__":
    unittest.main()
