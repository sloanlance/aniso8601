# -*- coding: utf-8 -*-

# This software may be modified and distributed under the terms
# of the BSD license.  See the LICENSE file for details.

from enum import Enum

class DateResolution(Enum):
    Year, Month, Week, Weekday, Day, Ordinal = range(6)

class TimeResolution(Enum):
    Seconds, Minutes, Hours = range(3)
