# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 07:10:52 2013

@author: daniel
"""

a = float(raw_input('dame un numero: '))

if a == 0 or 1/a < 1:
    print 'True'
else:
    print 'False, el resutado es: ', 1/a
    
if a != 0 and 1/a < 1:
    print 'True', 1/a
else:
    print 'False'
