#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 11:28:18 2017

@author: alw

SUBPROCESS_EXAMPLE.PY opens 3 subprocesses, reads a text file, trims each line to 5 characters, and sorts the trimmed lines.

Requires:
    read_file.py
    trim_record.py
    sort_file.py
"""

import subprocess

#This works:
#p1 = subprocess.Popen(['cat', 'haiku.txt'], stdout=subprocess.PIPE, universal_newlines=True)
#p2 = subprocess.Popen(['grep', 'Blue'], stdin=p1.stdout, stdout=subprocess.PIPE, universal_newlines=True)
#p3 = subprocess.Popen(['wc'], stdin=p2.stdout, stdout=subprocess.PIPE, universal_newlines=True)
#p1.stdout.close()
#p2.stdout.close()
#output = p3.communicate()[0]
#print(output)


#And finally so does this:
def more_processes(listofarguments, *args):
    if len(args) > 0:
        p = subprocess.Popen(listofarguments, stdin=args[0], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    else:
        p = subprocess.Popen(listofarguments, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    return p.stdout


p1 = more_processes(['python3', 'read_file.py', 'haiku.txt'])
p2 = more_processes(['python3', 'trim_record.py'], p1)
p3 = more_processes(['python3', 'sort_file.py'], p2)
print(p3.read())


p3.close()
p2.close()        
p1.close()

print('All Done!')