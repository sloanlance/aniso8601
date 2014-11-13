# -*- coding: utf-8 -*-

# Copyright (c) 2014, Brandon Nielsen
# All rights reserved.
#
# This software may be modified and distributed under the terms
# of the BSD license.  See the LICENSE file for details.

import datetime

def parse_timezone(tzstr):
    #tzstr can be ±hh:mm, ±hhmm, ±hh, the Z case is handled elsewhere

    tzstrlen = len(tzstr)

    if tzstrlen == 6:
        #±hh:mm
        tzhour = int(tzstr[1:3])
        tzminute = int(tzstr[4:6])

        if tzstr[0] == '+':
            return build_utcoffset(tzstr, datetime.timedelta(hours=tzhour, minutes=tzminute))
        else:
            if tzhour == 0 and tzminute == 0:
                raise ValueError('String is not a valid ISO8601 time offset.')
            else:
                return build_utcoffset(tzstr, -datetime.timedelta(hours=tzhour, minutes=tzminute))
    elif tzstrlen == 5:
        #±hhmm
        tzhour = int(tzstr[1:3])
        tzminute = int(tzstr[3:5])

        if tzstr[0] == '+':
            return build_utcoffset(tzstr, datetime.timedelta(hours=tzhour, minutes=tzminute))
        else:
            if tzhour == 0 and tzminute == 0:
                raise ValueError('String is not a valid ISO8601 time offset.')
            else:
                return build_utcoffset(tzstr, -datetime.timedelta(hours=tzhour, minutes=tzminute))
    elif tzstrlen == 3:
        #±hh
        tzhour = int(tzstr[1:3])

        if tzstr[0] == '+':
            return build_utcoffset(tzstr, datetime.timedelta(hours=tzhour))
        else:
            if tzhour == 0:
                raise ValueError('String is not a valid ISO8601 time offset.')
            else:
                return build_utcoffset(tzstr, -datetime.timedelta(hours=tzhour))
    else:
        raise ValueError('String is not a valid ISO8601 time offset.')

def build_utcoffset(name, utcdelta):
    #We build an offset in this manner since the
    #tzinfo class must have an init that can
    #"method that can be called with no arguments"

    returnoffset = UTCOffset()

    returnoffset.setname(name)
    returnoffset.setutcdelta(utcdelta)

    return returnoffset

class UTCOffset(datetime.tzinfo):
    def setname(self, name):
        self._name = name

    def setutcdelta(self, utcdelta):
        self._utcdelta = utcdelta

    def utcoffset(self, dt):
        return self._utcdelta

    def tzname(self, dt):
        return self._name

    def dst(self, dt):
        #ISO8601 specifies offsets should be different if DST is required,
        #instead of allowing for a DST to be specified
        return None
