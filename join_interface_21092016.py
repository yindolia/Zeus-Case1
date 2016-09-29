# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 16:21:01 2016

@author: ysingh2
"""

from itertools import groupby

t = open('C:/Users/ysingh2/Desktop/techs/t-interfac', 'w+')
with open('C:/Users/ysingh2/Desktop/techs/sample-interface.txt') as f:
    for key, group in groupby(f, lambda s: s.startswith('Ethernet1')):
        joinedLog= '\N'.join(s.rstrip('\n') for s in group)
        t.write(joinedLog)
        t.write('\n')
        print joinedLog
