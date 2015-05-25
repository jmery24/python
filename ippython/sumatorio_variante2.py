# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 07:04:20 2013

@author: daniel
"""

#programa:sumatorio_variante_2.py
#calcula el sumatorio de i

#data input
sum = 0
i = int(raw_input('valor de i: '))
lim = int(raw_input('valor de limite: '))

#procesing data
if i > lim:
    print 'el valor de <i> debe ser menor o igual al valor de <lim>'
else:
    while i <= lim:
        sum += i
        i += 1
    print 'el valor del sumatorio es %i ' %sum