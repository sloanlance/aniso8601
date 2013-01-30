import datetime

def parse_year(yearstr):
    #yearstr is of the format YYYY
    #
    #0000 (0 BC) is not representible as a datetime so a ValueError is raised
    #
    #Since no additional resolution is provided, the month is set to 1, and
    #day is set to 1.

    return datetime.date(int(yearstr), 1, 1)
