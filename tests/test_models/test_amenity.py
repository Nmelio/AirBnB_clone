#!/usr/bin/env python3
"""
Unittest implementation for Amenity class
"""
import unittest
from models.amenity import Amenity
import models.amenity


class TestAmenity(unittest.TestCase):
    """ This class test the ``Amenity`` class"""

    def test_attribute_name(self):
        """Test the attribute name"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")
        self.assertTrue(type(amenity.name) == str)

    def test_class_doc(self):
        """ Check for the class documentaion"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_module_doc(self):
        """ Check for the module documentation"""
        self.assertIsNotNone(models.amenity.__doc__)


if __name__ == "__main__":
    unittest.main()
