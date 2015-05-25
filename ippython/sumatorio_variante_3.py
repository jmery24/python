# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 07:12:49 2013

@author: daniel
"""

#programa:sumatorio_variante_3.py
#calcula el sumatorio de i

#data input
sum = 0
i = 2
lim = 0
while i > lim:
    i = int(raw_input('valor de i: '))
    lim = int(raw_input('valor de limite mayor o igual que <i>: '))
    
#procesing data
while i <= lim:
    sum += i
    i += 1
print 'el valor del sumatorio es %i ' %sum
