#!/usr/bin/env python3
"""
Unittest implementation for Review class
"""
import unittest
from models.review import Review
import models.review


class TestReview(unittest.TestCase):
    """ This class test the ``Review`` class"""

    def test_module_doc(self):
        """ Test for the existance of the module documentation"""
        self.assertIsNotNone(models.review.__doc__)

    def test_class_doc(self):
        """ Test for the ``Review`` class documentation"""
        self.assertIsNotNone(Review.__doc__)

    def test_attribute_place_id(self):
        """ Test with the place id"""
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertEqual(review.place_id, "")
        self.assertTrue(type(review.place_id) == str)

    def test_attribute_user_id(self):
        """ Test with the user ID"""
        review = Review()
        self.assertTrue(hasattr(review, "user_id"))
        self.assertEqual(review.user_id, "")
        self.assertTrue(type(review.user_id) == str)

    def test_attribute_text(self):
        """ Text with a review"""
        review = Review()
        self.assertTrue(hasattr(review, "text"))
        self.assertEqual(review.text, "")
        self.assertTrue(type(review.text) == str)


if __name__ == "__main__":
    unittest.main()
