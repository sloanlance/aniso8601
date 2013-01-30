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
    #day is set to 1.

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
