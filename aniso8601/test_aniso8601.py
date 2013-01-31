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
import aniso8601

class TestParseFunctions(unittest.TestCase):
    def test_parse_date(self):
        date = aniso8601.parse_date('2013')
        self.assertEqual(date.year, 2013)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 1)

        date = aniso8601.parse_date('0001')
        self.assertEqual(date.year, 1)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 1)

        date = aniso8601.parse_date('19')
        self.assertEqual(date.year, 1900)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 1)

        date = aniso8601.parse_date('1981-04-05')
        self.assertEqual(date.year, 1981)
        self.assertEqual(date.month, 4)
        self.assertEqual(date.day, 5)

        date = aniso8601.parse_date('19810405')
        self.assertEqual(date.year, 1981)
        self.assertEqual(date.month, 4)
        self.assertEqual(date.day, 5)

        date = aniso8601.parse_date('1981-04')
        self.assertEqual(date.year, 1981)
        self.assertEqual(date.month, 4)
        self.assertEqual(date.day, 1)

        date = aniso8601.parse_date('2004-W53')
        self.assertEqual(date.year, 2004)
        self.assertEqual(date.month, 12)
        self.assertEqual(date.weekday(), 0)

        date = aniso8601.parse_date('2009-W01')
        self.assertEqual(date.year, 2008)
        self.assertEqual(date.month, 12)
        self.assertEqual(date.weekday(), 0)

        date = aniso8601.parse_date('2004-W53-6')
        self.assertEqual(date.year, 2005)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 1)

        date = aniso8601.parse_date('2004W53')
        self.assertEqual(date.year, 2004)
        self.assertEqual(date.month, 12)
        self.assertEqual(date.weekday(), 0)

        date = aniso8601.parse_date('2004W536')
        self.assertEqual(date.year, 2005)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 1)

        date = aniso8601.parse_date('1981-095')
        self.assertEqual(date.year, 1981)
        self.assertEqual(date.month, 4)
        self.assertEqual(date.day, 5)

        date = aniso8601.parse_date('1981095')
        self.assertEqual(date.year, 1981)
        self.assertEqual(date.month, 4)
        self.assertEqual(date.day, 5)

    def test_parse_time(self):
        time = aniso8601.parse_time('01:23:45')
        self.assertEqual(time.hour, 1)
        self.assertEqual(time.minute, 23)
        self.assertEqual(time.second, 45)

        time = aniso8601.parse_time('24:00:00')
        self.assertEqual(time.hour, 0)
        self.assertEqual(time.minute, 0)
        self.assertEqual(time.second, 0)

        time = aniso8601.parse_time('23:21:28.512400')
        self.assertEqual(time.hour, 23)
        self.assertEqual(time.minute, 21)
        self.assertEqual(time.second, 28)
        self.assertEqual(time.microsecond, 512400)

        time = aniso8601.parse_time('01:23')
        self.assertEqual(time.hour, 1)
        self.assertEqual(time.minute, 23)

        time = aniso8601.parse_time('24:00')
        self.assertEqual(time.hour, 0)
        self.assertEqual(time.minute, 0)

        time = aniso8601.parse_time('01:23.4567')
        self.assertEqual(time.hour, 1)
        self.assertEqual(time.minute, 23)
        self.assertEqual(time.second, 27)
        self.assertEqual(time.microsecond, 402000)

        time = aniso8601.parse_time('012345')
        self.assertEqual(time.hour, 1)
        self.assertEqual(time.minute, 23)
        self.assertEqual(time.second, 45)

        time = aniso8601.parse_time('240000')
        self.assertEqual(time.hour, 0)
        self.assertEqual(time.minute, 0)
        self.assertEqual(time.second, 0)

        time = aniso8601.parse_time('0123')
        self.assertEqual(time.hour, 1)
        self.assertEqual(time.minute, 23)

        time = aniso8601.parse_time('2400')
        self.assertEqual(time.hour, 0)
        self.assertEqual(time.minute, 0)

        time = aniso8601.parse_time('01')
        self.assertEqual(time.hour, 1)

        time = aniso8601.parse_time('24')
        self.assertEqual(time.hour, 0)

        time = aniso8601.parse_time('232128.512400+00:00')
        self.assertEqual(time.hour, 23)
        self.assertEqual(time.minute, 21)
        self.assertEqual(time.second, 28)
        self.assertEqual(time.microsecond, 512400)
        tzinfoobject = time.tzinfo
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(hours=0))
        self.assertEqual(tzinfoobject.tzname(None), '+00:00')

        time = aniso8601.parse_time('0123.4567+00:00')
        self.assertEqual(time.hour, 1)
        self.assertEqual(time.minute, 23)
        self.assertEqual(time.second, 27)
        self.assertEqual(time.microsecond, 402000)
        tzinfoobject = time.tzinfo
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(hours=0))
        self.assertEqual(tzinfoobject.tzname(None), '+00:00')

        time = aniso8601.parse_time('01.4567+00:00')
        self.assertEqual(time.hour, 1)
        self.assertEqual(time.minute, 27)
        self.assertEqual(time.second, 24)
        self.assertEqual(time.microsecond, 120000)
        tzinfoobject = time.tzinfo
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(hours=0))
        self.assertEqual(tzinfoobject.tzname(None), '+00:00')

        time = aniso8601.parse_time('01:23:45+00:00')
        self.assertEqual(time.hour, 1)
        self.assertEqual(time.minute, 23)
        self.assertEqual(time.second, 45)
        tzinfoobject = time.tzinfo
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(hours=0))
        self.assertEqual(tzinfoobject.tzname(None), '+00:00')

        time = aniso8601.parse_time('24:00:00+00:00')
        self.assertEqual(time.hour, 0)
        self.assertEqual(time.minute, 0)
        self.assertEqual(time.second, 0)
        tzinfoobject = time.tzinfo
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(hours=0))
        self.assertEqual(tzinfoobject.tzname(None), '+00:00')

        time = aniso8601.parse_time('23:21:28.512400+00:00')
        self.assertEqual(time.hour, 23)
        self.assertEqual(time.minute, 21)
        self.assertEqual(time.second, 28)
        self.assertEqual(time.microsecond, 512400)
        tzinfoobject = time.tzinfo
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(hours=0))
        self.assertEqual(tzinfoobject.tzname(None), '+00:00')

        time = aniso8601.parse_time('01:23+00:00')
        self.assertEqual(time.hour, 1)
        self.assertEqual(time.minute, 23)
        tzinfoobject = time.tzinfo
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(hours=0))
        self.assertEqual(tzinfoobject.tzname(None), '+00:00')

        time = aniso8601.parse_time('24:00+00:00')
        self.assertEqual(time.hour, 0)
        self.assertEqual(time.minute, 0)
        tzinfoobject = time.tzinfo
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(hours=0))
        self.assertEqual(tzinfoobject.tzname(None), '+00:00')

        time = aniso8601.parse_time('01:23.4567+00:00')
        self.assertEqual(time.hour, 1)
        self.assertEqual(time.minute, 23)
        self.assertEqual(time.second, 27)
        self.assertEqual(time.microsecond, 402000)
        tzinfoobject = time.tzinfo
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(hours=0))
        self.assertEqual(tzinfoobject.tzname(None), '+00:00')

        time = aniso8601.parse_time('23:21:28.512400+11:15')
        self.assertEqual(time.hour, 23)
        self.assertEqual(time.minute, 21)
        self.assertEqual(time.second, 28)
        self.assertEqual(time.microsecond, 512400)
        tzinfoobject = time.tzinfo
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(hours=11, minutes=15))
        self.assertEqual(tzinfoobject.tzname(None), '+11:15')

        time = aniso8601.parse_time('23:21:28.512400-12:34')
        self.assertEqual(time.hour, 23)
        self.assertEqual(time.minute, 21)
        self.assertEqual(time.second, 28)
        self.assertEqual(time.microsecond, 512400)
        tzinfoobject = time.tzinfo
        self.assertEqual(tzinfoobject.utcoffset(None), -datetime.timedelta(hours=12, minutes=34))
        self.assertEqual(tzinfoobject.tzname(None), '-12:34')

        time = aniso8601.parse_time('23:21:28.512400Z')
        self.assertEqual(time.hour, 23)
        self.assertEqual(time.minute, 21)
        self.assertEqual(time.second, 28)
        self.assertEqual(time.microsecond, 512400)
        tzinfoobject = time.tzinfo
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(hours=0))
        self.assertEqual(tzinfoobject.tzname(None), 'UTC')

    def test_parse_datetime(self):
        resultdatetime = aniso8601.parse_datetime('1981-04-05T23:21:28.512400Z')
        self.assertEqual(resultdatetime.year, 1981)
        self.assertEqual(resultdatetime.month, 4)
        self.assertEqual(resultdatetime.day, 5)
        self.assertEqual(resultdatetime.hour, 23)
        self.assertEqual(resultdatetime.minute, 21)
        self.assertEqual(resultdatetime.second, 28)
        self.assertEqual(resultdatetime.microsecond, 512400)
        tzinfoobject = resultdatetime.tzinfo
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(hours=0))
        self.assertEqual(tzinfoobject.tzname(None), 'UTC')

        resultdatetime = aniso8601.parse_datetime('1981095T23:21:28.512400-12:34')
        self.assertEqual(resultdatetime.year, 1981)
        self.assertEqual(resultdatetime.month, 4)
        self.assertEqual(resultdatetime.day, 5)
        self.assertEqual(resultdatetime.hour, 23)
        self.assertEqual(resultdatetime.minute, 21)
        self.assertEqual(resultdatetime.second, 28)
        self.assertEqual(resultdatetime.microsecond, 512400)
        tzinfoobject = resultdatetime.tzinfo
        self.assertEqual(tzinfoobject.utcoffset(None), -datetime.timedelta(hours=12, minutes=34))
        self.assertEqual(tzinfoobject.tzname(None), '-12:34')

        resultdatetime = aniso8601.parse_datetime('19810405T23:21:28+00')
        self.assertEqual(resultdatetime.year, 1981)
        self.assertEqual(resultdatetime.month, 4)
        self.assertEqual(resultdatetime.day, 5)
        self.assertEqual(resultdatetime.hour, 23)
        self.assertEqual(resultdatetime.minute, 21)
        self.assertEqual(resultdatetime.second, 28)
        tzinfoobject = resultdatetime.tzinfo
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(hours=0))
        self.assertEqual(tzinfoobject.tzname(None), '+00')

        resultdatetime = aniso8601.parse_datetime('19810405T23:21:28+00:00')
        self.assertEqual(resultdatetime.year, 1981)
        self.assertEqual(resultdatetime.month, 4)
        self.assertEqual(resultdatetime.day, 5)
        self.assertEqual(resultdatetime.hour, 23)
        self.assertEqual(resultdatetime.minute, 21)
        self.assertEqual(resultdatetime.second, 28)
        tzinfoobject = resultdatetime.tzinfo
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(hours=0))
        self.assertEqual(tzinfoobject.tzname(None), '+00:00')

    def test_parse_datetime_spaceseperated(self):
        resultdatetime = aniso8601.parse_datetime('2004-W53-6 23:21:28.512400-12:34', ' ')
        self.assertEqual(resultdatetime.year, 2005)
        self.assertEqual(resultdatetime.month, 1)
        self.assertEqual(resultdatetime.day, 1)
        self.assertEqual(resultdatetime.hour, 23)
        self.assertEqual(resultdatetime.minute, 21)
        self.assertEqual(resultdatetime.second, 28)
        self.assertEqual(resultdatetime.microsecond, 512400)
        tzinfoobject = resultdatetime.tzinfo
        self.assertEqual(tzinfoobject.utcoffset(None), -datetime.timedelta(hours=12, minutes=34))
        self.assertEqual(tzinfoobject.tzname(None), '-12:34')

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

    def test_parse_ordinal_date(self):
        date = aniso8601.parse_ordinal_date('1981-095')
        self.assertEqual(date.year, 1981)
        self.assertEqual(date.month, 4)
        self.assertEqual(date.day, 5)

        date = aniso8601.parse_ordinal_date('1981095')
        self.assertEqual(date.year, 1981)
        self.assertEqual(date.month, 4)
        self.assertEqual(date.day, 5)

    def test_parse_time_naive(self):
        time = aniso8601.parse_time_naive('01:23:45')
        self.assertEqual(time.hour, 1)
        self.assertEqual(time.minute, 23)
        self.assertEqual(time.second, 45)

        time = aniso8601.parse_time_naive('24:00:00')
        self.assertEqual(time.hour, 0)
        self.assertEqual(time.minute, 0)
        self.assertEqual(time.second, 0)

        time = aniso8601.parse_time_naive('23:21:28.512400')
        self.assertEqual(time.hour, 23)
        self.assertEqual(time.minute, 21)
        self.assertEqual(time.second, 28)
        self.assertEqual(time.microsecond, 512400)

        time = aniso8601.parse_time_naive('01:23')
        self.assertEqual(time.hour, 1)
        self.assertEqual(time.minute, 23)

        time = aniso8601.parse_time_naive('24:00')
        self.assertEqual(time.hour, 0)
        self.assertEqual(time.minute, 0)

        time = aniso8601.parse_time_naive('01:23.4567')
        self.assertEqual(time.hour, 1)
        self.assertEqual(time.minute, 23)
        self.assertEqual(time.second, 27)
        self.assertEqual(time.microsecond, 402000)

        time = aniso8601.parse_time_naive('012345')
        self.assertEqual(time.hour, 1)
        self.assertEqual(time.minute, 23)
        self.assertEqual(time.second, 45)

        time = aniso8601.parse_time_naive('240000')
        self.assertEqual(time.hour, 0)
        self.assertEqual(time.minute, 0)
        self.assertEqual(time.second, 0)

        time = aniso8601.parse_time_naive('0123')
        self.assertEqual(time.hour, 1)
        self.assertEqual(time.minute, 23)

        time = aniso8601.parse_time_naive('2400')
        self.assertEqual(time.hour, 0)
        self.assertEqual(time.minute, 0)

        time = aniso8601.parse_time_naive('01')
        self.assertEqual(time.hour, 1)

        time = aniso8601.parse_time_naive('24')
        self.assertEqual(time.hour, 0)

        time = aniso8601.parse_time_naive('232128.512400')
        self.assertEqual(time.hour, 23)
        self.assertEqual(time.minute, 21)
        self.assertEqual(time.second, 28)
        self.assertEqual(time.microsecond, 512400)

        time = aniso8601.parse_time_naive('0123.4567')
        self.assertEqual(time.hour, 1)
        self.assertEqual(time.minute, 23)
        self.assertEqual(time.second, 27)
        self.assertEqual(time.microsecond, 402000)

        time = aniso8601.parse_time_naive('01.4567')
        self.assertEqual(time.hour, 1)
        self.assertEqual(time.minute, 27)
        self.assertEqual(time.second, 24)
        self.assertEqual(time.microsecond, 120000)

    def test_parse_timezone(self):
        tzinfoobject = aniso8601.parse_timezone('+00:00')
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(hours=0))
        self.assertEqual(tzinfoobject.tzname(None), '+00:00')

        tzinfoobject = aniso8601.parse_timezone('+01:00')
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(hours=1))
        self.assertEqual(tzinfoobject.tzname(None), '+01:00')

        tzinfoobject = aniso8601.parse_timezone('-01:00')
        self.assertEqual(tzinfoobject.utcoffset(None), -datetime.timedelta(hours=1))
        self.assertEqual(tzinfoobject.tzname(None), '-01:00')

        tzinfoobject = aniso8601.parse_timezone('+00:12')
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(minutes=12))
        self.assertEqual(tzinfoobject.tzname(None), '+00:12')

        tzinfoobject = aniso8601.parse_timezone('+01:23')
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(hours=1, minutes=23))
        self.assertEqual(tzinfoobject.tzname(None), '+01:23')

        tzinfoobject = aniso8601.parse_timezone('-01:23')
        self.assertEqual(tzinfoobject.utcoffset(None), -datetime.timedelta(hours=1, minutes=23))
        self.assertEqual(tzinfoobject.tzname(None), '-01:23')

        with self.assertRaises(ValueError):
            aniso8601.parse_timezone('-00:00')

        tzinfoobject = aniso8601.parse_timezone('+0000')
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(hours=0))
        self.assertEqual(tzinfoobject.tzname(None), '+0000')

        tzinfoobject = aniso8601.parse_timezone('+0100')
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(hours=1))
        self.assertEqual(tzinfoobject.tzname(None), '+0100')

        tzinfoobject = aniso8601.parse_timezone('-0100')
        self.assertEqual(tzinfoobject.utcoffset(None), -datetime.timedelta(hours=1))
        self.assertEqual(tzinfoobject.tzname(None), '-0100')

        tzinfoobject = aniso8601.parse_timezone('+0012')
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(minutes=12))
        self.assertEqual(tzinfoobject.tzname(None), '+0012')

        tzinfoobject = aniso8601.parse_timezone('+0123')
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(hours=1, minutes=23))
        self.assertEqual(tzinfoobject.tzname(None), '+0123')

        tzinfoobject = aniso8601.parse_timezone('-0123')
        self.assertEqual(tzinfoobject.utcoffset(None), -datetime.timedelta(hours=1, minutes=23))
        self.assertEqual(tzinfoobject.tzname(None), '-0123')

        with self.assertRaises(ValueError):
            aniso8601.parse_timezone('-0000')

        tzinfoobject = aniso8601.parse_timezone('+00')
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(hours=0))
        self.assertEqual(tzinfoobject.tzname(None), '+00')

        tzinfoobject = aniso8601.parse_timezone('+01')
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(hours=1))
        self.assertEqual(tzinfoobject.tzname(None), '+01')

        tzinfoobject = aniso8601.parse_timezone('-01')
        self.assertEqual(tzinfoobject.utcoffset(None), -datetime.timedelta(hours=1))
        self.assertEqual(tzinfoobject.tzname(None), '-01')

        tzinfoobject = aniso8601.parse_timezone('+12')
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(hours=12))
        self.assertEqual(tzinfoobject.tzname(None), '+12')

        tzinfoobject = aniso8601.parse_timezone('-12')
        self.assertEqual(tzinfoobject.utcoffset(None), -datetime.timedelta(hours=12))
        self.assertEqual(tzinfoobject.tzname(None), '-12')

        with self.assertRaises(ValueError):
            aniso8601.parse_timezone('-00')
