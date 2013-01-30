import unittest
import aniso8601

class TestParseFunctions(unittest.TestCase):
    def test_parse_year(self):
        date = aniso8601.parse_year('2013')
        self.assertEqual(date.year, 2013)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 1)

        date = aniso8601.parse_year('0001')
        self.assertEqual(date.year, 1)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 1)

        date = aniso8601.parse_year('19')
        self.assertEqual(date.year, 1900)
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

    def test_parse_week_date(self):
        date = aniso8601.parse_week_date('2004-W53')
        self.assertEqual(date.year, 2004)
        self.assertEqual(date.month, 12)
        self.assertEqual(date.weekday(), 0)

        date = aniso8601.parse_week_date('2009-W01')
        self.assertEqual(date.year, 2008)
        self.assertEqual(date.month, 12)
        self.assertEqual(date.weekday(), 0)

        date = aniso8601.parse_week_date('2009-W53')
        self.assertEqual(date.year, 2009)
        self.assertEqual(date.month, 12)
        self.assertEqual(date.weekday(), 0)

        date = aniso8601.parse_week_date('2010-W01')
        self.assertEqual(date.year, 2010)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.weekday(), 0)

        date = aniso8601.parse_week_date('2004-W53-6')
        self.assertEqual(date.year, 2005)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 1)

        date = aniso8601.parse_week_date('2009-W01-1')
        self.assertEqual(date.year, 2008)
        self.assertEqual(date.month, 12)
        self.assertEqual(date.day, 29)

        date = aniso8601.parse_week_date('2009-W53-7')
        self.assertEqual(date.year, 2010)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 3)

        date = aniso8601.parse_week_date('2010-W01-1')
        self.assertEqual(date.year, 2010)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 4)

        date = aniso8601.parse_week_date('2004W53')
        self.assertEqual(date.year, 2004)
        self.assertEqual(date.month, 12)
        self.assertEqual(date.weekday(), 0)

        date = aniso8601.parse_week_date('2009W01')
        self.assertEqual(date.year, 2008)
        self.assertEqual(date.month, 12)
        self.assertEqual(date.weekday(), 0)

        date = aniso8601.parse_week_date('2009W53')
        self.assertEqual(date.year, 2009)
        self.assertEqual(date.month, 12)
        self.assertEqual(date.weekday(), 0)

        date = aniso8601.parse_week_date('2010W01')
        self.assertEqual(date.year, 2010)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.weekday(), 0)

        date = aniso8601.parse_week_date('2004W536')
        self.assertEqual(date.year, 2005)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 1)

        date = aniso8601.parse_week_date('2009W011')
        self.assertEqual(date.year, 2008)
        self.assertEqual(date.month, 12)
        self.assertEqual(date.day, 29)

        date = aniso8601.parse_week_date('2009W537')
        self.assertEqual(date.year, 2010)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 3)

        date = aniso8601.parse_week_date('2010W011')
        self.assertEqual(date.year, 2010)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 4)
