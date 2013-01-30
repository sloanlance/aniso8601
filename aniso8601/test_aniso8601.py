import unittest
import aniso8601

class TestParseFunctions(unittest.TestCase):
    def test_parse_year(self):
        date = aniso8601.parse_year('2013')
        self.assertEqual(date.year, 2013)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 1)

        with self.assertRaises(ValueError):
            aniso8601.parse_year('0')

    def test_parse_calendar_date(self):
        date = aniso8601.parse_calendar_date('1981-04-05')
        self.assertEqual(date.year, 1981)
        self.assertEqual(date.month, 4)
        self.assertEqual(date.day, 5)

        date = aniso8601.parse_calendar_date('19810405')
        self.assertEqual(date.year, 1981)
        self.assertEqual(date.month, 4)
        self.assertEqual(date.day, 5)

        date = aniso8601.parse_calendar_date('1981-04')
        self.assertEqual(date.year, 1981)
        self.assertEqual(date.month, 4)
        self.assertEqual(date.day, 1)

        with self.assertRaises(ValueError):
            aniso8601.parse_calendar_date('198104')
