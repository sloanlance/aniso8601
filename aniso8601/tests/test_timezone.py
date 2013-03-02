# -*- coding: utf-8 -*-

#Copyright 2013 Brandon Nielsen
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import unittest
import datetime
import pickle

from aniso8601.timezone import parse_timezone, build_utcoffset

class TestTimezoneFunctions(unittest.TestCase):
    def test_parse_timezone(self):
        tzinfoobject = parse_timezone('+00:00')
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(hours=0))
        self.assertEqual(tzinfoobject.tzname(None), '+00:00')

        tzinfoobject = parse_timezone('+01:00')
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(hours=1))
        self.assertEqual(tzinfoobject.tzname(None), '+01:00')

        tzinfoobject = parse_timezone('-01:00')
        self.assertEqual(tzinfoobject.utcoffset(None), -datetime.timedelta(hours=1))
        self.assertEqual(tzinfoobject.tzname(None), '-01:00')

        tzinfoobject = parse_timezone('+00:12')
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(minutes=12))
        self.assertEqual(tzinfoobject.tzname(None), '+00:12')

        tzinfoobject = parse_timezone('+01:23')
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(hours=1, minutes=23))
        self.assertEqual(tzinfoobject.tzname(None), '+01:23')

        tzinfoobject = parse_timezone('-01:23')
        self.assertEqual(tzinfoobject.utcoffset(None), -datetime.timedelta(hours=1, minutes=23))
        self.assertEqual(tzinfoobject.tzname(None), '-01:23')

        with self.assertRaises(ValueError):
            parse_timezone('-00:00')

        tzinfoobject = parse_timezone('+0000')
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(hours=0))
        self.assertEqual(tzinfoobject.tzname(None), '+0000')

        tzinfoobject = parse_timezone('+0100')
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(hours=1))
        self.assertEqual(tzinfoobject.tzname(None), '+0100')

        tzinfoobject = parse_timezone('-0100')
        self.assertEqual(tzinfoobject.utcoffset(None), -datetime.timedelta(hours=1))
        self.assertEqual(tzinfoobject.tzname(None), '-0100')

        tzinfoobject = parse_timezone('+0012')
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(minutes=12))
        self.assertEqual(tzinfoobject.tzname(None), '+0012')

        tzinfoobject = parse_timezone('+0123')
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(hours=1, minutes=23))
        self.assertEqual(tzinfoobject.tzname(None), '+0123')

        tzinfoobject = parse_timezone('-0123')
        self.assertEqual(tzinfoobject.utcoffset(None), -datetime.timedelta(hours=1, minutes=23))
        self.assertEqual(tzinfoobject.tzname(None), '-0123')

        with self.assertRaises(ValueError):
            parse_timezone('-0000')

        tzinfoobject = parse_timezone('+00')
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(hours=0))
        self.assertEqual(tzinfoobject.tzname(None), '+00')

        tzinfoobject = parse_timezone('+01')
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(hours=1))
        self.assertEqual(tzinfoobject.tzname(None), '+01')

        tzinfoobject = parse_timezone('-01')
        self.assertEqual(tzinfoobject.utcoffset(None), -datetime.timedelta(hours=1))
        self.assertEqual(tzinfoobject.tzname(None), '-01')

        tzinfoobject = parse_timezone('+12')
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(hours=12))
        self.assertEqual(tzinfoobject.tzname(None), '+12')

        tzinfoobject = parse_timezone('-12')
        self.assertEqual(tzinfoobject.utcoffset(None), -datetime.timedelta(hours=12))
        self.assertEqual(tzinfoobject.tzname(None), '-12')

        with self.assertRaises(ValueError):
            parse_timezone('-00')

    def test_pickle(self):
        #Make sure timezone objects are pickleable
        testutcoffset = build_utcoffset('UTC', datetime.timedelta(0))

        utcoffsetpickle = pickle.dumps(testutcoffset)

        resultutcoffset = pickle.loads(utcoffsetpickle)

        self.assertEqual(resultutcoffset._name, testutcoffset._name)
        self.assertEqual(resultutcoffset._utcdelta, testutcoffset._utcdelta)
