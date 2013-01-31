===========
 aniso8601
===========

----------------------------------
Another ISO 8601 parser for Python
----------------------------------

Features
========
* Pure Python implementation
* No extra dependencies
* Logical behavior

 - Parse a time, get a `datetime.time <http://docs.python.org/2/library/datetime.html#datetime.time>`_
 - Parse a date, get a `datetime.date <http://docs.python.org/2/library/datetime.html#datetime.date>`_
 - Parse a date time, get a `datetime.datetime <http://docs.python.org/2/library/datetime.html#datetime.datetime>`_

* UTC offset represented as fixed-offset tzinfo
* No regular expressions

Use
===

Parsing datetimes
-----------------

To parse a typical ISO 8601 datetime string::

  >>> import aniso8601
  >>> aniso8601.parse_datetime('1977-06-10T12:00:00Z')
  datetime.datetime(1977, 6, 10, 12, 0, tzinfo=<aniso8601.UTCOffset object at 0x7f44fadbbd90>)

Alternative delimiters can be specified, for example, a space::

  >>> aniso8601.parse_datetime('1977-06-10 12:00:00Z', delimiter=' ')
  datetime.datetime(1977, 6, 10, 12, 0, tzinfo=<aniso8601.UTCOffset object at 0x7f44fadbbf50>)

UTC offsets are supported::

  >>> aniso8601.parse_datetime('1979-06-05T08:00:00-08:00')
  datetime.datetime(1979, 6, 5, 8, 0, tzinfo=<aniso8601.UTCOffset object at 0x7f44fadbbf50>)

If a UTC offset is not specified, the returned datetime will be naive::

  >>> aniso8601.parse_datetime('1983-01-22T08:00:00')
  datetime.datetime(1983, 1, 22, 8, 0)

Parsing dates
-------------

To parse a date represented in an ISO 8601 string::

  >>> import aniso8601
  >>> aniso8601.parse_date('1984-04-23')
  datetime.date(1984, 4, 23)

Basic format is supported as well::

  >>> aniso8601.parse_date('19840423')
  datetime.date(1984, 4, 23)

To parse a date using the ISO 8601 week date format::

  >>> aniso8601.parse_date('1986-W38-1')
  datetime.date(1986, 9, 15)

To parse an ISO 8601 ordinal date::

  >>> aniso8601.parse_date('1988-132')
  datetime.date(1988, 5, 11)

Parsing times
-------------

To parse a time formatted as an ISO 8601 string::

  >>> import aniso8601
  >>> aniso8601.parse_time('11:31:14')
  datetime.time(11, 31, 14)

As with all of the above, basic format is supported::

  >>> aniso8601.parse_time('113114')
  datetime.time(11, 31, 14)

A UTC offset can be specified for times::

  >>> aniso8601.parse_time('17:18:19-02:30')
  datetime.time(17, 18, 19, tzinfo=<aniso8601.UTCOffset object at 0x7f44fad82c50>)
  >>> aniso8601.parse_time('171819Z')
  datetime.time(17, 18, 19, tzinfo=<aniso8601.UTCOffset object at 0x7f44fadbbd90>)

Reduced accuracy is supported::

  >>> aniso8601.parse_time('21:42')
  datetime.time(21, 42)
  >>> aniso8601.parse_time('22')
  datetime.time(22, 0)

A decimal fraction is always allowed on the lowest order element of an ISO 8601 formatted time::

  >>> aniso8601.parse_time('22:33.5')
  datetime.time(22, 33, 30)
  >>> aniso8601.parse_time('23.75')
  datetime.time(23, 45)

Tests
=====

To run the unit tests::

   $ python -m unittest aniso8601.test_aniso8601

References
==========

* `ISO 8601:2004(E) <http://dotat.at/tmp/ISO_8601-2004_E.pdf>`_ (Caution, PDF link)
* `Wikipedia article on ISO 8601 <http://en.wikipedia.org/wiki/Iso8601>`_
* `Discussion on alternative ISO 8601 parsers for Python <https://groups.google.com/forum/#!topic/comp.lang.python/Q2w4R89Nq1w>`_
