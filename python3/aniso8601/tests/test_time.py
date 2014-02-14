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

from aniso8601.time import parse_time, parse_datetime, parse_time_naive

class TestTimeFunctions(unittest.TestCase):
    def test_parse_time(self):
        time = parse_time('01:23:45')
        self.assertEqual(time.hour, 1)
        self.assertEqual(time.minute, 23)
        self.assertEqual(time.second, 45)

        time = parse_time('24:00:00')
        self.assertEqual(time.hour, 0)
        self.assertEqual(time.minute, 0)
        self.assertEqual(time.second, 0)

        time = parse_time('23:21:28.512400')
        self.assertEqual(time.hour, 23)
        self.assertEqual(time.minute, 21)
        self.assertEqual(time.second, 28)
        self.assertEqual(time.microsecond, 512400)

        time = parse_time('01:23')
        self.assertEqual(time.hour, 1)
        self.assertEqual(time.minute, 23)

        time = parse_time('24:00')
        self.assertEqual(time.hour, 0)
        self.assertEqual(time.minute, 0)

        time = parse_time('01:23.4567')
        self.assertEqual(time.hour, 1)
        self.assertEqual(time.minute, 23)
        self.assertEqual(time.second, 27)
        self.assertEqual(time.microsecond, 402000)

        time = parse_time('012345')
        self.assertEqual(time.hour, 1)
        self.assertEqual(time.minute, 23)
        self.assertEqual(time.second, 45)

        time = parse_time('240000')
        self.assertEqual(time.hour, 0)
        self.assertEqual(time.minute, 0)
        self.assertEqual(time.second, 0)

        time = parse_time('0123')
        self.assertEqual(time.hour, 1)
        self.assertEqual(time.minute, 23)

        time = parse_time('2400')
        self.assertEqual(time.hour, 0)
        self.assertEqual(time.minute, 0)

        time = parse_time('01')
        self.assertEqual(time.hour, 1)

        time = parse_time('24')
        self.assertEqual(time.hour, 0)

        time = parse_time('12.5')
        self.assertEqual(time.hour, 12)
        self.assertEqual(time.minute, 30)

        time = parse_time('232128.512400+00:00')
        self.assertEqual(time.hour, 23)
        self.assertEqual(time.minute, 21)
        self.assertEqual(time.second, 28)
        self.assertEqual(time.microsecond, 512400)
        tzinfoobject = time.tzinfo
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(hours=0))
        self.assertEqual(tzinfoobject.tzname(None), '+00:00')

        time = parse_time('0123.4567+00:00')
        self.assertEqual(time.hour, 1)
        self.assertEqual(time.minute, 23)
        self.assertEqual(time.second, 27)
        self.assertEqual(time.microsecond, 402000)
        tzinfoobject = time.tzinfo
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(hours=0))
        self.assertEqual(tzinfoobject.tzname(None), '+00:00')

        time = parse_time('01.4567+00:00')
        self.assertEqual(time.hour, 1)
        self.assertEqual(time.minute, 27)
        self.assertEqual(time.second, 24)
        self.assertEqual(time.microsecond, 120000)
        tzinfoobject = time.tzinfo
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(hours=0))
        self.assertEqual(tzinfoobject.tzname(None), '+00:00')

        time = parse_time('01:23:45+00:00')
        self.assertEqual(time.hour, 1)
        self.assertEqual(time.minute, 23)
        self.assertEqual(time.second, 45)
        tzinfoobject = time.tzinfo
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(hours=0))
        self.assertEqual(tzinfoobject.tzname(None), '+00:00')

        time = parse_time('24:00:00+00:00')
        self.assertEqual(time.hour, 0)
        self.assertEqual(time.minute, 0)
        self.assertEqual(time.second, 0)
        tzinfoobject = time.tzinfo
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(hours=0))
        self.assertEqual(tzinfoobject.tzname(None), '+00:00')

        time = parse_time('23:21:28.512400+00:00')
        self.assertEqual(time.hour, 23)
        self.assertEqual(time.minute, 21)
        self.assertEqual(time.second, 28)
        self.assertEqual(time.microsecond, 512400)
        tzinfoobject = time.tzinfo
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(hours=0))
        self.assertEqual(tzinfoobject.tzname(None), '+00:00')

        time = parse_time('01:23+00:00')
        self.assertEqual(time.hour, 1)
        self.assertEqual(time.minute, 23)
        tzinfoobject = time.tzinfo
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(hours=0))
        self.assertEqual(tzinfoobject.tzname(None), '+00:00')

        time = parse_time('24:00+00:00')
        self.assertEqual(time.hour, 0)
        self.assertEqual(time.minute, 0)
        tzinfoobject = time.tzinfo
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(hours=0))
        self.assertEqual(tzinfoobject.tzname(None), '+00:00')

        time = parse_time('01:23.4567+00:00')
        self.assertEqual(time.hour, 1)
        self.assertEqual(time.minute, 23)
        self.assertEqual(time.second, 27)
        self.assertEqual(time.microsecond, 402000)
        tzinfoobject = time.tzinfo
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(hours=0))
        self.assertEqual(tzinfoobject.tzname(None), '+00:00')

        time = parse_time('23:21:28.512400+11:15')
        self.assertEqual(time.hour, 23)
        self.assertEqual(time.minute, 21)
        self.assertEqual(time.second, 28)
        self.assertEqual(time.microsecond, 512400)
        tzinfoobject = time.tzinfo
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(hours=11, minutes=15))
        self.assertEqual(tzinfoobject.tzname(None), '+11:15')

        time = parse_time('23:21:28.512400-12:34')
        self.assertEqual(time.hour, 23)
        self.assertEqual(time.minute, 21)
        self.assertEqual(time.second, 28)
        self.assertEqual(time.microsecond, 512400)
        tzinfoobject = time.tzinfo
        self.assertEqual(tzinfoobject.utcoffset(None), -datetime.timedelta(hours=12, minutes=34))
        self.assertEqual(tzinfoobject.tzname(None), '-12:34')

        time = parse_time('23:21:28.512400Z')
        self.assertEqual(time.hour, 23)
        self.assertEqual(time.minute, 21)
        self.assertEqual(time.second, 28)
        self.assertEqual(time.microsecond, 512400)
        tzinfoobject = time.tzinfo
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(hours=0))
        self.assertEqual(tzinfoobject.tzname(None), 'UTC')

        time = parse_time('06:14:00.000123Z')
        self.assertEqual(time.hour, 6)
        self.assertEqual(time.minute, 14)
        self.assertEqual(time.second, 00)
        self.assertEqual(time.microsecond, 123)
        tzinfoobject = time.tzinfo
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(hours=0))
        self.assertEqual(tzinfoobject.tzname(None), 'UTC')

    def test_parse_datetime(self):
        resultdatetime = parse_datetime('1981-04-05T23:21:28.512400Z')
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

        resultdatetime = parse_datetime('1981095T23:21:28.512400-12:34')
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

        resultdatetime = parse_datetime('19810405T23:21:28+00')
        self.assertEqual(resultdatetime.year, 1981)
        self.assertEqual(resultdatetime.month, 4)
        self.assertEqual(resultdatetime.day, 5)
        self.assertEqual(resultdatetime.hour, 23)
        self.assertEqual(resultdatetime.minute, 21)
        self.assertEqual(resultdatetime.second, 28)
        tzinfoobject = resultdatetime.tzinfo
        self.assertEqual(tzinfoobject.utcoffset(None), datetime.timedelta(hours=0))
        self.assertEqual(tzinfoobject.tzname(None), '+00')

        resultdatetime = parse_datetime('19810405T23:21:28+00:00')
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
        resultdatetime = parse_datetime('2004-W53-6 23:21:28.512400-12:34', ' ')
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

    def test_parse_time_naive(self):
        time = parse_time_naive('01:23:45')
        self.assertEqual(time.hour, 1)
        self.assertEqual(time.minute, 23)
        self.assertEqual(time.second, 45)

        time = parse_time_naive('24:00:00')
        self.assertEqual(time.hour, 0)
        self.assertEqual(time.minute, 0)
        self.assertEqual(time.second, 0)

        time = parse_time_naive('23:21:28.512400')
        self.assertEqual(time.hour, 23)
        self.assertEqual(time.minute, 21)
        self.assertEqual(time.second, 28)
        self.assertEqual(time.microsecond, 512400)

        time = parse_time_naive('01:23')
        self.assertEqual(time.hour, 1)
        self.assertEqual(time.minute, 23)

        time = parse_time_naive('24:00')
        self.assertEqual(time.hour, 0)
        self.assertEqual(time.minute, 0)

        time = parse_time_naive('01:23.4567')
        self.assertEqual(time.hour, 1)
        self.assertEqual(time.minute, 23)
        self.assertEqual(time.second, 27)
        self.assertEqual(time.microsecond, 402000)

        time = parse_time_naive('012345')
        self.assertEqual(time.hour, 1)
        self.assertEqual(time.minute, 23)
        self.assertEqual(time.second, 45)

        time = parse_time_naive('240000')
        self.assertEqual(time.hour, 0)
        self.assertEqual(time.minute, 0)
        self.assertEqual(time.second, 0)

        time = parse_time_naive('0123')
        self.assertEqual(time.hour, 1)
        self.assertEqual(time.minute, 23)

        time = parse_time_naive('2400')
        self.assertEqual(time.hour, 0)
        self.assertEqual(time.minute, 0)

        time = parse_time_naive('01')
        self.assertEqual(time.hour, 1)

        time = parse_time_naive('24')
        self.assertEqual(time.hour, 0)

        time = parse_time_naive('232128.512400')
        self.assertEqual(time.hour, 23)
        self.assertEqual(time.minute, 21)
        self.assertEqual(time.second, 28)
        self.assertEqual(time.microsecond, 512400)

        time = parse_time_naive('0123.4567')
        self.assertEqual(time.hour, 1)
        self.assertEqual(time.minute, 23)
        self.assertEqual(time.second, 27)
        self.assertEqual(time.microsecond, 402000)

        time = parse_time_naive('01.4567')
        self.assertEqual(time.hour, 1)
        self.assertEqual(time.minute, 27)
        self.assertEqual(time.second, 24)
        self.assertEqual(time.microsecond, 120000)
