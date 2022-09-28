import unittest
from Sorting import sort_main_file

class TestParsing(unittest.TestCase):
    def test_parsing(self):
        self.assertEqual(sort_main_file(), 0)