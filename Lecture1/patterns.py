#!/usr/bin/env python

# The 'getlines' program which processes lines.

import fileinput
import re

for line in fileinput.input():
    if re.search( "TCGGGG", line ):
        print( line.rstrip()  )
