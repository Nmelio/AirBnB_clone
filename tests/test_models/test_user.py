#!/usr/bin/env python3
"""
Unittest implementation for User model
"""
import unittest
from models.user import User
import models.user


class TestUser(unittest.TestCase):
    """Test User class"""

    def test_module_doc(self):
        """ Test for the module's documentation"""
        self.assertIsNotNone(models.user.__doc__)

    def test_class_doc(self):
        """ Test for the class documentation"""
        self.assertIsNotNone(User.__doc__)

    def test_attribute_email(self):
        """ Test with adding user's email"""
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertEqual(user.email, "")
        self.assertTrue(type(user.email) == str)

    def test_attribute_password(self):
        """Test with adding user's password"""
        user = User()
        self.assertTrue(hasattr(user, "password"))
        self.assertEqual(user.password, "")
        self.assertTrue(type(user.password) == str)

    def test_attribute_first_name(self):
        """ Test with adding user's first name"""
        user = User()
        self.assertTrue(hasattr(user, "first_name"))
        self.assertEqual(user.first_name, "")
        self.assertTrue(type(user.first_name) == str)

    def test_attribute_last_name(self):
        """ Test with user's last name"""
        user = User()
        self.assertTrue(hasattr(user, "last_name"))
        self.assertEqual(user.last_name, "")
        self.assertTrue(type(user.last_name) == str)


if __name__ == "__main__":
    unittest.main()