#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 11:28:18 2017

@author: alw
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




#This does, but it is really slow.
p1 = subprocess.Popen(['python3', 'read_file.py', 'haiku.txt'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

while p1.poll() == None:
    for line in p1.stdout:
        print(line)
        p1.stdout.flush()
        
p1.stdout.close()
print('All Done!')


#p2 = subprocess.Popen(['python3', 'trim_record.py', '5'], stdin=p1.stdout, stdout=subprocess.PIPE, bufsize=1, universal_newlines=True)
#print('p1: ', p1.stdout.readline())
#print('p2: ', p2.stdout)