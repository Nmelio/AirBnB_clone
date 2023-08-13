#!/usr/bin/env python3
"""
Unittest implementation for State model
"""
import unittest
from models.state import State
import models.state


class TestState(unittest.TestCase):
    """ Test the ``State`` class"""

    def test_module_doc(self):
        """ Test for the module documentation"""
        self.assertIsNotNone(models.state.__doc__)

    def test_class_doc(self):
        """ Test for the class documentation"""
        self.assertIsNotNone(State.__doc__)

    def test_attribute_name(self):
        """ Test using the name"""
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")


if __name__ == "__main__":
    unittest.main()
