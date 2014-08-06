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

from aniso8601.duration import parse_duration, parse_duration_prescribed, parse_duration_combined, _parse_duration_element

class TestDurationFunctions(unittest.TestCase):
    def test_parse_duration(self):
        resultduration = parse_duration('P1Y2M3DT4H54M6S')
        self.assertEqual(resultduration.days, 428)
        self.assertEqual(resultduration.seconds, 17646)

        resultduration = parse_duration('P1Y2M3DT4H54M6.5S')
        self.assertEqual(resultduration.days, 428)
        self.assertEqual(resultduration.seconds, 17646)
        self.assertEqual(resultduration.microseconds, 500000)

        resultduration = parse_duration('P1Y2M3DT4H54M6,5S')
        self.assertEqual(resultduration.days, 428)
        self.assertEqual(resultduration.seconds, 17646)
        self.assertEqual(resultduration.microseconds, 500000)

        resultduration = parse_duration('P1Y2M3D')
        self.assertEqual(resultduration.days, 428)

        resultduration = parse_duration('P1Y2M3.5D')
        self.assertEqual(resultduration.days, 428)
        self.assertEqual(resultduration.seconds, 43200)

        resultduration = parse_duration('P1Y2M3,5D')
        self.assertEqual(resultduration.days, 428)
        self.assertEqual(resultduration.seconds, 43200)

        resultduration = parse_duration('PT4H54M6.5S')
        self.assertEqual(resultduration.days, 0)
        self.assertEqual(resultduration.seconds, 17646)
        self.assertEqual(resultduration.microseconds, 500000)

        resultduration = parse_duration('PT4H54M6,5S')
        self.assertEqual(resultduration.days, 0)
        self.assertEqual(resultduration.seconds, 17646)
        self.assertEqual(resultduration.microseconds, 500000)

        resultduration = parse_duration('P1Y')
        self.assertEqual(resultduration.days, 365)

        resultduration = parse_duration('P1.5Y')
        self.assertEqual(resultduration.days, 547)
        self.assertEqual(resultduration.seconds, 43200)

        resultduration = parse_duration('P1,5Y')
        self.assertEqual(resultduration.days, 547)
        self.assertEqual(resultduration.seconds, 43200)

        resultduration = parse_duration('P1M')
        self.assertEqual(resultduration.days, 30)

        resultduration = parse_duration('P1.5M')
        self.assertEqual(resultduration.days, 45)

        resultduration = parse_duration('P1,5M')
        self.assertEqual(resultduration.days, 45)

        resultduration = parse_duration('P1W')
        self.assertEqual(resultduration.days, 7)

        resultduration = parse_duration('P1.5W')
        self.assertEqual(resultduration.days, 10)
        self.assertEqual(resultduration.seconds, 43200)

        resultduration = parse_duration('P1,5W')
        self.assertEqual(resultduration.days, 10)
        self.assertEqual(resultduration.seconds, 43200)

        resultduration = parse_duration('P1D')
        self.assertEqual(resultduration.days, 1)

        resultduration = parse_duration('P1.5D')
        self.assertEqual(resultduration.days, 1)
        self.assertEqual(resultduration.seconds, 43200)

        resultduration = parse_duration('P1,5D')
        self.assertEqual(resultduration.days, 1)
        self.assertEqual(resultduration.seconds, 43200)

        resultduration = parse_duration('P0003-06-04T12:30:05')
        self.assertEqual(resultduration.days, 1279)
        self.assertEqual(resultduration.seconds, 45005)
        self.assertEqual(resultduration.microseconds, 0)

        resultduration = parse_duration('P0003-06-04T12:30:05.5')
        self.assertEqual(resultduration.days, 1279)
        self.assertEqual(resultduration.seconds, 45005)
        self.assertEqual(resultduration.microseconds, 500000)

        #Verify overflows
        self.assertEqual(parse_duration('PT36H'), parse_duration('P1DT12H'))

    def test_parse_duration_prescribed(self):
        with self.assertRaises(ValueError):
            parse_duration_prescribed('P1Y2M3DT4H5.1234M6.1234S')

        with self.assertRaises(ValueError):
            parse_duration_prescribed('P1Y2M3DT4H5.1234M6S')

        resultduration = parse_duration_prescribed('P1Y2M3DT4H54M6S')
        self.assertEqual(resultduration.days, 428)
        self.assertEqual(resultduration.seconds, 17646)

        resultduration = parse_duration_prescribed('P1Y2M3DT4H54M6.5S')
        self.assertEqual(resultduration.days, 428)
        self.assertEqual(resultduration.seconds, 17646)
        self.assertEqual(resultduration.microseconds, 500000)

        resultduration = parse_duration_prescribed('P1Y2M3DT4H54M6,5S')
        self.assertEqual(resultduration.days, 428)
        self.assertEqual(resultduration.seconds, 17646)
        self.assertEqual(resultduration.microseconds, 500000)

        resultduration = parse_duration_prescribed('P1Y2M3D')
        self.assertEqual(resultduration.days, 428)

        resultduration = parse_duration_prescribed('P1Y2M3.5D')
        self.assertEqual(resultduration.days, 428)
        self.assertEqual(resultduration.seconds, 43200)

        resultduration = parse_duration_prescribed('P1Y2M3,5D')
        self.assertEqual(resultduration.days, 428)
        self.assertEqual(resultduration.seconds, 43200)

        resultduration = parse_duration_prescribed('PT4H54M6.5S')
        self.assertEqual(resultduration.days, 0)
        self.assertEqual(resultduration.seconds, 17646)
        self.assertEqual(resultduration.microseconds, 500000)

        resultduration = parse_duration_prescribed('PT4H54M6,5S')
        self.assertEqual(resultduration.days, 0)
        self.assertEqual(resultduration.seconds, 17646)
        self.assertEqual(resultduration.microseconds, 500000)

        resultduration = parse_duration_prescribed('P1Y')
        self.assertEqual(resultduration.days, 365)

        resultduration = parse_duration_prescribed('P1.5Y')
        self.assertEqual(resultduration.days, 547)
        self.assertEqual(resultduration.seconds, 43200)

        resultduration = parse_duration_prescribed('P1,5Y')
        self.assertEqual(resultduration.days, 547)
        self.assertEqual(resultduration.seconds, 43200)

        resultduration = parse_duration_prescribed('P1M')
        self.assertEqual(resultduration.days, 30)

        resultduration = parse_duration_prescribed('P1.5M')
        self.assertEqual(resultduration.days, 45)

        resultduration = parse_duration_prescribed('P1,5M')
        self.assertEqual(resultduration.days, 45)

        resultduration = parse_duration_prescribed('P1W')
        self.assertEqual(resultduration.days, 7)

        resultduration = parse_duration_prescribed('P1.5W')
        self.assertEqual(resultduration.days, 10)
        self.assertEqual(resultduration.seconds, 43200)

        resultduration = parse_duration_prescribed('P1,5W')
        self.assertEqual(resultduration.days, 10)
        self.assertEqual(resultduration.seconds, 43200)

        resultduration = parse_duration_prescribed('P1D')
        self.assertEqual(resultduration.days, 1)

        resultduration = parse_duration_prescribed('P1.5D')
        self.assertEqual(resultduration.days, 1)
        self.assertEqual(resultduration.seconds, 43200)

        resultduration = parse_duration_prescribed('P1,5D')
        self.assertEqual(resultduration.days, 1)
        self.assertEqual(resultduration.seconds, 43200)

        #Verify overflows
        self.assertEqual(parse_duration('PT36H'), parse_duration('P1DT12H'))

    def test_parse_duration_combined(self):
        resultduration = parse_duration_combined('P0003-06-04T12:30:05')
        self.assertEqual(resultduration.days, 1279)
        self.assertEqual(resultduration.seconds, 45005)
        self.assertEqual(resultduration.microseconds, 0)

        resultduration = parse_duration_combined('P0003-06-04T12:30:05.5')
        self.assertEqual(resultduration.days, 1279)
        self.assertEqual(resultduration.seconds, 45005)
        self.assertEqual(resultduration.microseconds, 500000)

    def test_parse_duration_element(self):
        self.assertEqual(_parse_duration_element('P1Y2M3D', 'Y'), 1)
        self.assertEqual(_parse_duration_element('P1Y2M3D', 'M'), 2)
        self.assertEqual(_parse_duration_element('P1Y2M3D', 'D'), 3)
        self.assertEqual(_parse_duration_element('T4H5M6.1234S', 'H'), 4)
        self.assertEqual(_parse_duration_element('T4H5M6.1234S', 'M'), 5)
        self.assertEqual(_parse_duration_element('T4H5M6.1234S', 'S'), 6.1234)
        self.assertEqual(_parse_duration_element('PT4H54M6,5S', 'H'), 4)
        self.assertEqual(_parse_duration_element('PT4H54M6,5S', 'M'), 54)
        self.assertEqual(_parse_duration_element('PT4H54M6,5S', 'S'), 6.5)
