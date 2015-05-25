# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 07:15:24 2013

@author: daniel
"""

#data input
a = int(raw_input('Elige un numero <A>: '))
b = int(raw_input('Elige un numero <B>: '))

#proccesing
if a > b:
    maximo = a
else:
    maximo = b
    
#printout
print 'el maximo es ', maximo
