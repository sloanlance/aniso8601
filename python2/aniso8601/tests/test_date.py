# -*- coding: utf-8 -*-

# Copyright (c) 2014, Brandon Nielsen
# All rights reserved.
#
# This software may be modified and distributed under the terms
# of the BSD license.  See the LICENSE file for details.

import unittest

from aniso8601.date import parse_date, parse_year, parse_calendar_date, parse_week_date, parse_ordinal_date

class TestDateFunctions(unittest.TestCase):
    def test_parse_date(self):
        date = parse_date('2013')
        self.assertEqual(date.year, 2013)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 1)

        date = parse_date('0001')
        self.assertEqual(date.year, 1)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 1)

        date = parse_date('19')
        self.assertEqual(date.year, 1900)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 1)

        date = parse_date('1981-04-05')
        self.assertEqual(date.year, 1981)
        self.assertEqual(date.month, 4)
        self.assertEqual(date.day, 5)

        date = parse_date('19810405')
        self.assertEqual(date.year, 1981)
        self.assertEqual(date.month, 4)
        self.assertEqual(date.day, 5)

        date = parse_date('1981-04')
        self.assertEqual(date.year, 1981)
        self.assertEqual(date.month, 4)
        self.assertEqual(date.day, 1)

        date = parse_date('2004-W53')
        self.assertEqual(date.year, 2004)
        self.assertEqual(date.month, 12)
        self.assertEqual(date.weekday(), 0)

        date = parse_date('2009-W01')
        self.assertEqual(date.year, 2008)
        self.assertEqual(date.month, 12)
        self.assertEqual(date.weekday(), 0)

        date = parse_date('2004-W53-6')
        self.assertEqual(date.year, 2005)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 1)

        date = parse_date('2004W53')
        self.assertEqual(date.year, 2004)
        self.assertEqual(date.month, 12)
        self.assertEqual(date.weekday(), 0)

        date = parse_date('2004W536')
        self.assertEqual(date.year, 2005)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 1)

        date = parse_date('1981-095')
        self.assertEqual(date.year, 1981)
        self.assertEqual(date.month, 4)
        self.assertEqual(date.day, 5)

        date = parse_date('1981095')
        self.assertEqual(date.year, 1981)
        self.assertEqual(date.month, 4)
        self.assertEqual(date.day, 5)

    def test_parse_year(self):
        date = parse_year('2013')
        self.assertEqual(date.year, 2013)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 1)

        date = parse_year('0001')
        self.assertEqual(date.year, 1)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 1)

        date = parse_year('19')
        self.assertEqual(date.year, 1900)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 1)

        with self.assertRaises(ValueError):
            parse_year('0')

    def test_parse_calendar_date(self):
        date = parse_calendar_date('1981-04-05')
        self.assertEqual(date.year, 1981)
        self.assertEqual(date.month, 4)
        self.assertEqual(date.day, 5)

        date = parse_calendar_date('19810405')
        self.assertEqual(date.year, 1981)
        self.assertEqual(date.month, 4)
        self.assertEqual(date.day, 5)

        date = parse_calendar_date('1981-04')
        self.assertEqual(date.year, 1981)
        self.assertEqual(date.month, 4)
        self.assertEqual(date.day, 1)

        with self.assertRaises(ValueError):
            parse_calendar_date('198104')

    def test_parse_week_date(self):
        date = parse_week_date('2004-W53')
        self.assertEqual(date.year, 2004)
        self.assertEqual(date.month, 12)
        self.assertEqual(date.weekday(), 0)

        date = parse_week_date('2009-W01')
        self.assertEqual(date.year, 2008)
        self.assertEqual(date.month, 12)
        self.assertEqual(date.weekday(), 0)

        date = parse_week_date('2009-W53')
        self.assertEqual(date.year, 2009)
        self.assertEqual(date.month, 12)
        self.assertEqual(date.weekday(), 0)

        date = parse_week_date('2010-W01')
        self.assertEqual(date.year, 2010)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.weekday(), 0)

        date = parse_week_date('2004-W53-6')
        self.assertEqual(date.year, 2005)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 1)

        date = parse_week_date('2009-W01-1')
        self.assertEqual(date.year, 2008)
        self.assertEqual(date.month, 12)
        self.assertEqual(date.day, 29)

        date = parse_week_date('2009-W53-7')
        self.assertEqual(date.year, 2010)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 3)

        date = parse_week_date('2010-W01-1')
        self.assertEqual(date.year, 2010)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 4)

        date = parse_week_date('2004W53')
        self.assertEqual(date.year, 2004)
        self.assertEqual(date.month, 12)
        self.assertEqual(date.weekday(), 0)

        date = parse_week_date('2009W01')
        self.assertEqual(date.year, 2008)
        self.assertEqual(date.month, 12)
        self.assertEqual(date.weekday(), 0)

        date = parse_week_date('2009W53')
        self.assertEqual(date.year, 2009)
        self.assertEqual(date.month, 12)
        self.assertEqual(date.weekday(), 0)

        date = parse_week_date('2010W01')
        self.assertEqual(date.year, 2010)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.weekday(), 0)

        date = parse_week_date('2004W536')
        self.assertEqual(date.year, 2005)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 1)

        date = parse_week_date('2009W011')
        self.assertEqual(date.year, 2008)
        self.assertEqual(date.month, 12)
        self.assertEqual(date.day, 29)

        date = parse_week_date('2009W537')
        self.assertEqual(date.year, 2010)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 3)

        date = parse_week_date('2010W011')
        self.assertEqual(date.year, 2010)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 4)

    def test_parse_ordinal_date(self):
        date = parse_ordinal_date('1981-095')
        self.assertEqual(date.year, 1981)
        self.assertEqual(date.month, 4)
        self.assertEqual(date.day, 5)

        date = parse_ordinal_date('1981095')
        self.assertEqual(date.year, 1981)
        self.assertEqual(date.month, 4)
        self.assertEqual(date.day, 5)
