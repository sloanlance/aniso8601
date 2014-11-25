# -*- coding: utf-8 -*-

# Copyright (c) 2014, Brandon Nielsen
# All rights reserved.
#
# This software may be modified and distributed under the terms
# of the BSD license.  See the LICENSE file for details.

import datetime

from .timezone import parse_timezone, build_utcoffset
from .date import parse_date
from .resolution import TimeResolution

def get_resolution(isotimestr):
    #Valid time formats are:
    #
    #hh:mm:ss
    #hhmmss
    #hh:mm
    #hhmm
    #hh
    #hh:mm:ssZ
    #hhmmssZ
    #hh:mmZ
    #hhmmZ
    #hhZ
    #hh:mm:ss±hh:mm
    #hhmmss±hh:mm
    #hh:mm±hh:mm
    #hhmm±hh:mm
    #hh±hh:mm
    #hh:mm:ss±hhmm
    #hhmmss±hhmm
    #hh:mm±hhmm
    #hhmm±hhmm
    #hh±hhmm
    #hh:mm:ss±hh
    #hhmmss±hh
    #hh:mm±hh
    #hhmm±hh
    #hh±hh

    #Split the string at the TZ, if necessary
    if isotimestr.find('+') != -1:
        timestr = isotimestr[0:isotimestr.find('+')]
    elif isotimestr.find('-') != -1:
        timestr = isotimestr[0:isotimestr.find('-')]
    elif isotimestr.endswith('Z'):
        timestr = isotimestr[:-1]
    else:
        timestr = isotimestr

    if timestr.count(':') == 2:
        #hh:mm:ss
        return TimeResolution.Seconds
    elif timestr.count(':') == 1:
        #hh:mm
        return TimeResolution.Minutes

    #Format must be hhmmss, hhmm, or hh
    if timestr.find('.') == -1:
        #No time fractions
        timestrlen = len(timestr)
    else:
        #The lowest order element is a fraction
        timestrlen = len(timestr.split('.')[0])

    if timestrlen == 6:
        #hhmmss
        return TimeResolution.Seconds
    elif timestrlen == 4:
        #hhmm
        return TimeResolution.Minutes
    elif timestrlen == 2:
        #hh
        return TimeResolution.Hours
    else:
        raise ValueError('String is not a valid ISO8601 time.')

def parse_time(isotimestr):
    #Given a string in any ISO8601 time format, return a datetime.time object
    #that corresponds to the given time. Fixed offset tzdata will be included
    #if UTC offset is given in the input string. Valid time formats are:
    #
    #hh:mm:ss
    #hhmmss
    #hh:mm
    #hhmm
    #hh
    #hh:mm:ssZ
    #hhmmssZ
    #hh:mmZ
    #hhmmZ
    #hhZ
    #hh:mm:ss±hh:mm
    #hhmmss±hh:mm
    #hh:mm±hh:mm
    #hhmm±hh:mm
    #hh±hh:mm
    #hh:mm:ss±hhmm
    #hhmmss±hhmm
    #hh:mm±hhmm
    #hhmm±hhmm
    #hh±hhmm
    #hh:mm:ss±hh
    #hhmmss±hh
    #hh:mm±hh
    #hhmm±hh
    #hh±hh

    #Split the string at the TZ, if necessary
    if isotimestr.find('+') != -1:
        timestr = isotimestr[0:isotimestr.find('+')]
        tzstr = isotimestr[isotimestr.find('+'):]
    elif isotimestr.find('-') != -1:
        timestr = isotimestr[0:isotimestr.find('-')]
        tzstr = isotimestr[isotimestr.find('-'):]
    elif isotimestr.endswith('Z'):
        timestr = isotimestr[:-1]
        tzstr = 'Z'
    else:
        timestr = isotimestr
        tzstr = None

    if tzstr == None:
        return parse_time_naive(timestr)
    elif tzstr == 'Z':
        return parse_time_naive(timestr).replace(tzinfo=build_utcoffset('UTC', datetime.timedelta(hours=0)))
    else:
        return parse_time_naive(timestr).replace(tzinfo=parse_timezone(tzstr))

def parse_datetime(isodatetimestr, delimiter='T'):
    #Given a string in ISO8601 date time format, return a datetime.datetime
    #object that corresponds to the given date time.
    #By default, the ISO8601 specified T delimiter is used to split the
    #date and time (<date>T<time>). Fixed offset tzdata will be included
    #if UTC offset is given in the input string.

    isodatestr, isotimestr = isodatetimestr.split(delimiter)

    datepart = parse_date(isodatestr)
    timepart = parse_time(isotimestr)

    return datetime.datetime.combine(datepart, timepart)

def parse_time_naive(timestr):
    #timestr is of the format hh:mm:ss, hh:mm, hhmmss, hhmm, hh
    #
    #hh is between 0 and 24, 24 is not allowed in the Python time format, since
    #it represents midnight, a time of 00:00:00 is returned
    #
    #mm is between 0 and 60, with 60 used to denote a leap second
    #
    #No tzinfo will be included

    if timestr.count(':') == 2:
        #hh:mm:ss
        timestrarray = timestr.split(':')

        isohour = int(timestrarray[0])
        isominute = int(timestrarray[1])

        if isominute > 60:
            raise ValueError('String is not a valid ISO8601 time.')

        if isohour == 24:
            return datetime.time(hour=0, minute=0)

        #Since the time constructor doesn't handle fractional seconds, we put
        #the seconds in to a timedelta, and add it to the time before returning
        secondsdelta = datetime.timedelta(seconds = float(timestrarray[2]))

        #Now combine todays date (just so we have a date object), the time, the
        #delta, and return the time component
        return (datetime.datetime.combine(datetime.date.today(), datetime.time(hour=isohour, minute=isominute)) + secondsdelta).time()
    elif timestr.count(':') == 1:
        #hh:mm
        timestrarray = timestr.split(':')

        isohour = int(timestrarray[0])
        isominute = float(timestrarray[1]) #Minute may now be a fraction

        if isominute > 60:
            raise ValueError('String is not a valid ISO8601 time.')

        if isohour == 24:
            return datetime.time(hour=0, minute=0)

        #Since the time constructor doesn't handle fractional minutes, we put
        #the minutes in to a timedelta, and add it to the time before returning
        minutesdelta = datetime.timedelta(minutes = isominute)

        #Now combine todays date (just so we have a date object), the time, the
        #delta, and return the time component
        return (datetime.datetime.combine(datetime.date.today(), datetime.time(hour=isohour)) + minutesdelta).time()
    else:
        #Format must be hhmmss, hhmm, or hh
        if timestr.find('.') == -1:
            #No time fractions
            timestrlen = len(timestr)

            if timestrlen == 6:
                #hhmmss
                isohour = int(timestr[0:2])
                isominute = int(timestr[2:4])
                isosecond = int(timestr[4:6])

                if isominute > 60:
                    raise ValueError('String is not a valid ISO8601 time.')

                if isohour == 24:
                    return datetime.time(hour=0, minute=0)

                return datetime.time(hour=isohour, minute=isominute, second=isosecond)
            elif timestrlen == 4:
                #hhmm
                isohour = int(timestr[0:2])
                isominute = int(timestr[2:4])

                if isominute > 60:
                    raise ValueError('String is not a valid ISO8601 time.')

                if isohour == 24:
                    return datetime.time(hour=0, minute=0)

                return datetime.time(hour=isohour, minute=isominute)
            elif timestrlen == 2:
                #hh
                isohour = int(timestr[0:2])

                if isohour == 24:
                    return datetime.time(hour=0)

                return datetime.time(hour=isohour)
            else:
                raise ValueError('String is not a valid ISO8601 time.')
        else:
            #The lowest order element is a fraction
            timestrlen = len(timestr.split('.')[0])

            if timestrlen == 6:
                #hhmmss.
                isohour = int(timestr[0:2])
                isominute = int(timestr[2:4])

                if isominute > 60:
                    raise ValueError('String is not a valid ISO8601 time.')

                if isohour == 24:
                    return datetime.time(hour=0, minute=0)

                #Since the time constructor doesn't handle fractional seconds, we put
                #the seconds in to a timedelta, and add it to the time before returning
                secondsdelta = datetime.timedelta(seconds = float(timestr[4:]))

                #Now combine todays date (just so we have a date object), the time, the
                #delta, and return the time component
                return (datetime.datetime.combine(datetime.date.today(), datetime.time(hour=isohour, minute=isominute)) + secondsdelta).time()
            elif timestrlen == 4:
                #hhmm.
                isohour = int(timestr[0:2])
                isominute = float(timestr[2:])

                if isominute > 60:
                    raise ValueError('String is not a valid ISO8601 time.')

                if isohour == 24:
                    return datetime.time(hour=0, minute=0)

                #Since the time constructor doesn't handle fractional minutes, we put
                #the minutes in to a timedelta, and add it to the time before returning
                minutesdelta = datetime.timedelta(minutes = isominute)

                #Now combine todays date (just so we have a date object), the time, the
                #delta, and return the time component
                return (datetime.datetime.combine(datetime.date.today(), datetime.time(hour=isohour)) + minutesdelta).time()
            elif timestrlen == 2:
                #hh.
                isohour = float(timestr)

                if isohour == 24:
                    return datetime.time(hour=0, minute=0)

                #Since the time constructor doesn't handle fractional hours, we put
                #the hours in to a timedelta, and add it to the time before returning
                hoursdelta = datetime.timedelta(hours = isohour)

                #Now combine todays date (just so we have a date object), the time, the
                #delta, and return the time component
                return (datetime.datetime.combine(datetime.date.today(), datetime.time(hour=0)) + hoursdelta).time()
