# -*- coding: utf-8 -*-

# Copyright (c) 2014, Brandon Nielsen
# All rights reserved.
#
# This software may be modified and distributed under the terms
# of the BSD license.  See the LICENSE file for details.

import unittest

from aniso8601.duration import parse_duration, _parse_duration_prescribed, _parse_duration_combined, _parse_duration_element

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

    def test_parse_duration_relative(self):
        resultduration = parse_duration('P1Y2M3DT4H54M6.5S', relative=True)
        self.assertEqual(resultduration.years, 1)
        self.assertEqual(resultduration.months, 2)
        self.assertEqual(resultduration.days, 3)
        self.assertEqual(resultduration.hours, 4)
        self.assertEqual(resultduration.minutes, 54)
        self.assertEqual(resultduration.seconds, 6.5)

        resultduration = parse_duration('P0003-06-04T12:30:05.5', relative=True)
        self.assertEqual(resultduration.years, 3)
        self.assertEqual(resultduration.months, 6)
        self.assertEqual(resultduration.days, 4)
        self.assertEqual(resultduration.hours, 12)
        self.assertEqual(resultduration.minutes, 30)
        self.assertEqual(resultduration.seconds, 5)
        self.assertEqual(resultduration.microseconds, 500000)

    def test_parse_duration_prescribed(self):
        with self.assertRaises(ValueError):
            _parse_duration_prescribed('P1Y2M3DT4H5.1234M6.1234S', False)

        with self.assertRaises(ValueError):
            _parse_duration_prescribed('P1Y2M3DT4H5.1234M6S', False)

        resultduration = _parse_duration_prescribed('P1Y2M3DT4H54M6S', False)
        self.assertEqual(resultduration.days, 428)
        self.assertEqual(resultduration.seconds, 17646)

        resultduration = _parse_duration_prescribed('P1Y2M3DT4H54M6.5S', False)
        self.assertEqual(resultduration.days, 428)
        self.assertEqual(resultduration.seconds, 17646)
        self.assertEqual(resultduration.microseconds, 500000)

        resultduration = _parse_duration_prescribed('P1Y2M3DT4H54M6,5S', False)
        self.assertEqual(resultduration.days, 428)
        self.assertEqual(resultduration.seconds, 17646)
        self.assertEqual(resultduration.microseconds, 500000)

        resultduration = _parse_duration_prescribed('P1Y2M3D', False)
        self.assertEqual(resultduration.days, 428)

        resultduration = _parse_duration_prescribed('P1Y2M3.5D', False)
        self.assertEqual(resultduration.days, 428)
        self.assertEqual(resultduration.seconds, 43200)

        resultduration = _parse_duration_prescribed('P1Y2M3,5D', False)
        self.assertEqual(resultduration.days, 428)
        self.assertEqual(resultduration.seconds, 43200)

        resultduration = _parse_duration_prescribed('PT4H54M6.5S', False)
        self.assertEqual(resultduration.days, 0)
        self.assertEqual(resultduration.seconds, 17646)
        self.assertEqual(resultduration.microseconds, 500000)

        resultduration = _parse_duration_prescribed('PT4H54M6,5S', False)
        self.assertEqual(resultduration.days, 0)
        self.assertEqual(resultduration.seconds, 17646)
        self.assertEqual(resultduration.microseconds, 500000)

        resultduration = _parse_duration_prescribed('P1Y', False)
        self.assertEqual(resultduration.days, 365)

        resultduration = _parse_duration_prescribed('P1.5Y', False)
        self.assertEqual(resultduration.days, 547)
        self.assertEqual(resultduration.seconds, 43200)

        resultduration = _parse_duration_prescribed('P1,5Y', False)
        self.assertEqual(resultduration.days, 547)
        self.assertEqual(resultduration.seconds, 43200)

        resultduration = _parse_duration_prescribed('P1M', False)
        self.assertEqual(resultduration.days, 30)

        resultduration = _parse_duration_prescribed('P1.5M', False)
        self.assertEqual(resultduration.days, 45)

        resultduration = _parse_duration_prescribed('P1,5M', False)
        self.assertEqual(resultduration.days, 45)

        resultduration = _parse_duration_prescribed('P1W', False)
        self.assertEqual(resultduration.days, 7)

        resultduration = _parse_duration_prescribed('P1.5W', False)
        self.assertEqual(resultduration.days, 10)
        self.assertEqual(resultduration.seconds, 43200)

        resultduration = _parse_duration_prescribed('P1,5W', False)
        self.assertEqual(resultduration.days, 10)
        self.assertEqual(resultduration.seconds, 43200)

        resultduration = _parse_duration_prescribed('P1D', False)
        self.assertEqual(resultduration.days, 1)

        resultduration = _parse_duration_prescribed('P1.5D', False)
        self.assertEqual(resultduration.days, 1)
        self.assertEqual(resultduration.seconds, 43200)

        resultduration = _parse_duration_prescribed('P1,5D', False)
        self.assertEqual(resultduration.days, 1)
        self.assertEqual(resultduration.seconds, 43200)

        #Verify overflows
        self.assertEqual(parse_duration('PT36H', False), parse_duration('P1DT12H', False))

    def test_parse_duration_prescribed_relative(self):
        with self.assertRaises(ValueError):
            _parse_duration_prescribed('P1Y2M3DT4H5.1234M6.1234S', True)

        with self.assertRaises(ValueError):
            _parse_duration_prescribed('P1Y2M3DT4H5.1234M6S', True)

        #Fractional months and years are not defined
        #https://github.com/dateutil/dateutil/issues/40
        with self.assertRaises(ValueError):
            _parse_duration_prescribed('P1.5Y', True)

        with self.assertRaises(ValueError):
            _parse_duration_prescribed('P1.5M', True)

        resultduration = _parse_duration_prescribed('P1Y', True)
        self.assertEqual(resultduration.years, 1)

        resultduration = _parse_duration_prescribed('P1M', True)
        self.assertEqual(resultduration.months, 1)

        #Add the relative ‘days’ argument to the absolute day. Notice that the ‘weeks’ argument is multiplied by 7 and added to ‘days’.
        #http://dateutil.readthedocs.org/en/latest/relativedelta.html
        resultduration = _parse_duration_prescribed('P1W', True)
        self.assertEqual(resultduration.days, 7)

        resultduration = _parse_duration_prescribed('P1.5W', True)
        self.assertEqual(resultduration.days, 10.5) #Fractional weeks are allowed

    def test_parse_duration_combined(self):
        resultduration = _parse_duration_combined('P0003-06-04T12:30:05', False)
        self.assertEqual(resultduration.days, 1279)
        self.assertEqual(resultduration.seconds, 45005)
        self.assertEqual(resultduration.microseconds, 0)

        resultduration = _parse_duration_combined('P0003-06-04T12:30:05.5', False)
        self.assertEqual(resultduration.days, 1279)
        self.assertEqual(resultduration.seconds, 45005)
        self.assertEqual(resultduration.microseconds, 500000)

    def test_parse_duration_combined_relative(self):
        resultduration = _parse_duration_combined('P0003-06-04T12:30:05', True)
        self.assertEqual(resultduration.years, 3)
        self.assertEqual(resultduration.months, 6)
        self.assertEqual(resultduration.days, 4)
        self.assertEqual(resultduration.hours, 12)
        self.assertEqual(resultduration.minutes, 30)
        self.assertEqual(resultduration.seconds, 5)

        resultduration = _parse_duration_combined('P0003-06-04T12:30:05.5', True)
        self.assertEqual(resultduration.years, 3)
        self.assertEqual(resultduration.months, 6)
        self.assertEqual(resultduration.days, 4)
        self.assertEqual(resultduration.hours, 12)
        self.assertEqual(resultduration.minutes, 30)
        self.assertEqual(resultduration.seconds, 5)
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
