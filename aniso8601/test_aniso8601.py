import unittest
import aniso8601

class TestParseFunctions(unittest.TestCase):
    def test_parse_year(self):
        date = aniso8601.parse_year('2013')
        self.assertEqual(date.year, 2013)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 1)
