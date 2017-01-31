#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 15:35:03 2017

@author: alw
"""

import sys

ntrim = sys.argv[1]
record_trimmed = sys.argv[2][:ntrim]
print (record_trimmed)