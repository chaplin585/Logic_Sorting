import unittest
from Parsingfile import main

class TestParsing(unittest.TestCase):
    def test_parsing(self):
        self.assertEqual(main(), 0)