# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 09:17:59 2013

@author: daniel
"""

edad_1 = int(raw_input("edad persona 1: "))
edad_2 = int(raw_input("edad persona 2: "))

if edad_1 == edad_2:
    print "Tienen la misma edad"
else:
    if edad_1 < edad_2:
        print "persona 1 menor que persona 2"
    else:
        print "persona 1 mayor que persona 2"
    