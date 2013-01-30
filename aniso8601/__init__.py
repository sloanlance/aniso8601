import datetime

def parse_year(yearstr):
    #yearstr is of the format Y[YYY]
    #
    #0000 (1 BC) is not representible as a Python date so a ValueError is
    #raised
    #
    #Truncated dates, like '19', refer to 1900-1999 inclusive, we simply parse
    #to 1900-01-01
    #
    #Since no additional resolution is provided, the month is set to 1, and
    #day is set to 1

    if len(yearstr) == 4:
        return datetime.date(int(yearstr), 1, 1)
    else:
        #Shift 0s in from the left to form complete year
        return datetime.date(int(yearstr.ljust(4, '0')), 1, 1)

def parse_calendar_date(datestr):
    #datestr is of the format YYYY-MM-DD, YYYYMMDD, or YYYY-MM
    datestrlen = len(datestr)

    if datestrlen == 10:
        #YYYY-MM-DD
        parseddatetime = datetime.datetime.strptime(datestr, '%Y-%m-%d')

        #Since no 'time' is given, cast to a date
        return parseddatetime.date()
    elif datestrlen == 8:
        #YYYYMMDD
        parseddatetime = datetime.datetime.strptime(datestr, '%Y%m%d')

        #Since no 'time' is given, cast to a date
        return parseddatetime.date()
    elif datestrlen == 7:
        #YYYY-MM
        parseddatetime = datetime.datetime.strptime(datestr, '%Y-%m')

        #Since no 'time' is given, cast to a date
        return parseddatetime.date()
    else:
        raise ValueError('String is not a valid ISO8601 calendar date.')

def parse_week_date(datestr):
    #datestr is of the format YYYY-Www, YYYYWww, YYYY-Www-D, YYYYWwwD
    #
    #W is the week number prefix, ww is the week number, between 1 and 53
    #0 is not a valid week number, which differs from the Python implementation
    #
    #D is the weekday number, between 1 and 7, which differs from the Python
    #implementation which is between 0 and 6

    isoyear = int(datestr[0:4])
    gregorianyearstart = _iso_year_start(isoyear)

    #Week number will be the two characters after the W
    windex = datestr.find('W')
    isoweeknumber = int(datestr[windex + 1:windex + 3])

    if isoweeknumber == 0:
        raise ValueError('00 is not a valid ISO8601 weeknumber.')

    datestrlen = len(datestr)

    if datestr.find('-') != -1:
        if datestrlen == 8:
            #YYYY-Www
            #Suss out the date
            return gregorianyearstart + datetime.timedelta(weeks=isoweeknumber - 1, days=0)
        elif datestrlen == 10:
            #YYYY-Www-D
            isoday = int(datestr[9:10])

            return gregorianyearstart + datetime.timedelta(weeks=isoweeknumber - 1, days=isoday - 1)
        else:
            raise ValueError('String is not a valid ISO8601 week date.')
    else:
        if datestrlen == 7:
            #YYYYWww
            return gregorianyearstart + datetime.timedelta(weeks=isoweeknumber - 1, days=0)
        elif datestrlen == 8:
            #YYYYWwwD
            isoday = int(datestr[7:8])

            return gregorianyearstart + datetime.timedelta(weeks=isoweeknumber - 1, days=isoday - 1)
        else:
            raise ValueError('String is not a valid ISO8601 week date.')

def _iso_year_start(isoyear):
    #Given an ISO year, returns the equivalent of the start of the year on the
    #Gregorian calendar (which is used by Python)
    #Stolen from:
    #http://stackoverflow.com/questions/304256/whats-the-best-way-to-find-the-inverse-of-datetime-isocalendar

    #Determine the location of the 4th of January, the first week of the ISO
    #year in the week containing the 4th of January
    #http://en.wikipedia.org/wiki/ISO_week_date
    fourth_jan = datetime.date(isoyear, 1, 4)

    #Note the conversion from ISO day (1 - 7) and Python day (0 - 6)
    delta = datetime.timedelta(fourth_jan.isoweekday() - 1)

    #Return the start of the year
    return fourth_jan - delta
