#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 13:40:41 2017

@author: alw

READ_FILE.PY reads a specified text file when entered in the commandline in a subprocess by subprocess_example.py
"""

import sys

if len(sys.argv) >= 2:
    file = open(sys.argv[1])
else:
    file = open('haiku.txt')
       

for line in file:
    print(line.strip()),
    sys.stdout.flush()
    

file.close()
 