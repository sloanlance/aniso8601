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

from duration import parse_duration
from time import parse_datetime
from date import parse_date

def parse_interval(isointervalstr, intervaldelimiter='/', datetimedelimiter='T'):
    #Given a string representing an ISO8601 interval, return a
    #tuple of datetime.date or date.datetime objects representing the beginning
    #and end of the specified interval. Valid formats are:
    #
    #<start>/<end>
    #<start>/<duration>
    #<duration>/<end>
    #
    #The <start> and <end> values can represent dates, or datetimes,
    #not times.
    #
    #The format:
    #
    #<duration>
    #
    #Is expressly not supported as there is no way to provide the addtional
    #required context.

    firstpart, secondpart = isointervalstr.split(intervaldelimiter)

    if firstpart[0] == 'P':
        #<duration>/<end>
        #Notice that these are not returned 'in order' (earlier to later), this
        #is to maintain consistency with parsing <start>/<end> durations, as
        #well as making repeating interval code cleaner. Users who desire
        #durations to be in order can use the 'sorted' operator.

        #We need to figure out if <end> is a date, or a datetime
        if secondpart.find(datetimedelimiter) != -1:
            #<end> is a datetime
            duration = parse_duration(firstpart)
            enddatetime = parse_datetime(secondpart, delimiter=datetimedelimiter)

            return (enddatetime, enddatetime - duration)
        else:
            #<end> must just be a date
            duration = parse_duration(firstpart)
            enddate = parse_date(secondpart)

            return (enddate, enddate - duration)
    elif secondpart[0] == 'P':
        #<start>/<duration>
        #We need to figure out if <start> is a date, or a datetime
        if firstpart.find(datetimedelimiter) != -1:
            #<end> is a datetime
            duration = parse_duration(secondpart)
            startdatetime = parse_datetime(firstpart, delimiter=datetimedelimiter)

            return (startdatetime, startdatetime + duration)
        else:
            #<start> must just be a date
            duration = parse_duration(secondpart)
            startdate = parse_date(firstpart)

            return (startdate, startdate + duration)
    else:
        #<start>/<end>
        if firstpart.find(datetimedelimiter) != -1 and secondpart.find(datetimedelimiter) != -1:
            #Both parts are datetimes
            return (parse_datetime(firstpart, delimiter=datetimedelimiter), parse_datetime(secondpart, delimiter=datetimedelimiter))
        elif firstpart.find(datetimedelimiter) != -1 and secondpart.find(datetimedelimiter) == -1:
            #First part is a datetime, second part is a date
            return (parse_datetime(firstpart, delimiter=datetimedelimiter), parse_date(secondpart))
        elif firstpart.find(datetimedelimiter) == -1 and secondpart.find(datetimedelimiter) != -1:
            #First part is a date, second part is a datetime
            return (parse_date(firstpart), parse_datetime(secondpart, delimiter=datetimedelimiter))
        else:
            #Both parts are dates
            return (parse_date(firstpart), parse_date(secondpart))

def parse_repeating_interval(isointervalstr, intervaldelimiter='/', datetimedelimiter='T'):
    #Given a string representing an ISO8601 interval repating, return a
    #generator of datetime.date or date.datetime objects representing the
    #dates specified by the repeating interval. Valid formats are:
    #
    #Rnn/<interval>
    #R/<interval>

    if isointervalstr[0] != 'R':
        raise ValueError('String is not a valid ISO8601 repeating interval.')

    #Parse the number of iterations
    iterationpart, intervalpart = isointervalstr.split(intervaldelimiter, 1)

    if len(iterationpart) > 1:
        iterations = int(iterationpart[1:])
    else:
        iterations = None

    interval = parse_interval(intervalpart, intervaldelimiter, datetimedelimiter)

    intervaltimedelta = interval[1] - interval[0]

    #Now, build and return the generator
    if iterations != None:
        return date_generator(interval[0], intervaltimedelta, iterations)
    else:
        return date_generator_unbounded(interval[0], intervaltimedelta)

def date_generator(startdate, timedelta, iterations):
    currentdate = startdate
    currentiteration = 0

    while currentiteration < iterations:
        yield currentdate

        #Update the values
        currentdate += timedelta
        currentiteration += 1

def date_generator_unbounded(startdate, timedelta):
    currentdate = startdate

    while True:
        yield currentdate

        #Update the value
        currentdate += timedelta
