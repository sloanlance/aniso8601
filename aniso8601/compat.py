#!/usr/bin/env python

import sys

PY2 = sys.version_info[0] == 2

if PY2:
    range = xrange
else:
    range = range
