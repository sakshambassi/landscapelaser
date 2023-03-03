""" Tests for sharpness

To run all tests inside directory Tests/, 
run `python -m unittest discover tests` from the repo directory

"""
import unittest

from landscapelaser import LandscapeLaser

class TestArgs(unittest.TestCase):
    def test_calculate_none_args_exception(self):
        """ Tests calculate() ValueError raise
        """
        ll = LandscapeLaser()
        self.assertRaises(ValueError, ll.calculate, None, None)