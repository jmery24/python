# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 06:48:34 2013

@author: daniel
"""

#programa:sumatorio_variante_1.py
#calcula el sumatorio de i

#data input
sum = 0
i = int(raw_input('valor de i: '))
lim = int(raw_input('valor de limite: '))

#procesing data
while i <= lim:
    sum += i
    i += 1
    
#printout
print 'el valor del sumatorio es %i ' %sum