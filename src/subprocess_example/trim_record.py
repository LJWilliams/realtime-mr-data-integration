#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 15:35:03 2017

@author: alw

TRIM_RECORD.PY trims file read in from stdin as in a subprocess by subprocess_example.py

"""

import sys

for line in sys.stdin:
    print(line.strip()[:5]), # explicitly set to 5 characters because when ntrim set as variable, the correct output wouldn't return.  Any suggestions?
    sys.stdout.flush()

    