import datetime

def parse_year(yearstr):
    #yearstr is of the format YYYY
    #
    #0000 (0 BC) is not representible as a datetime so a ValueError is raised
    #
    #Since no additional resolution is provided, the month is set to 1, and
    #day is set to 1.

    return datetime.date(int(yearstr), 1, 1)

def parse_calendar_date(datestr):
    #datestr is of the format YYYY-MM-DD, YYYYMMDD, or YYYY-MM
    datestrlen = len(datestr)

    if datestrlen == 10:
        #YYYY-MM-DD
        parseddatetime = datetime.datetime.strptime(datestr, '%Y-%m-%d')

        #Since no 'time' is given, cast to a date
        return datetime.date(parseddatetime.year, parseddatetime.month, parseddatetime.day)
    elif datestrlen == 8:
        #YYYYMMDD
        parseddatetime = datetime.datetime.strptime(datestr, '%Y%m%d')

        #Since no 'time' is given, cast to a date
        return datetime.date(parseddatetime.year, parseddatetime.month, parseddatetime.day)
    elif datestrlen == 7:
        #YYYY-MM
        parseddatetime = datetime.datetime.strptime(datestr, '%Y-%m')

        #Since no 'time' is given, cast to a date
        return datetime.date(parseddatetime.year, parseddatetime.month, parseddatetime.day)
    else:
        raise ValueError('String is not a valid ISO8601 calendar date.')
