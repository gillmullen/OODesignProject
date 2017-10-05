""" Test Module; Test the readme is non empty. """

import unittest

class readmeTestCase(unittest.TestCase):
    """Test Case class for to_string method"""

    def test_notempty(self):
        """Test case A. readme_notempty"""
        f = open('readme.md', 'r')
	self.assertNotEqual(f.read(), '')

if __name__ == '__main__':
    unittest.main()  # run all tests
