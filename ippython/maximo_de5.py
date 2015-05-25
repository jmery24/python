# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 07:33:52 2013

@author: daniel
"""

#data input
a = int(raw_input('Elige un numero <A>: '))
b = int(raw_input('Elige un numero <B>: '))
c = int(raw_input('Elige un numero <C>: '))
d = int(raw_input('Elige un numero <D>: '))
e = int(raw_input('Elige un numero <E>: '))

#proccesing
if a > b:
    maximo = a
else:
    maximo = b
if c > maximo:
    maximo = c
else:
    maximo = maximo
if d > maximo:
    maximo = d
else:
    maximo = maximo
if e > maximo:
    maximo = e
else:
    maximo = maximo
    
#printout
print 'el maximo es ', maximo