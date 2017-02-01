#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 14:15:53 2017

@author: alw

SORT_FILE.PY sorts file read in from stdin as in a subprocess by subprocess_example.py
"""

import sys

record = []

for line in sys.stdin:
    record.append(line)
record.sort()
print(record)
