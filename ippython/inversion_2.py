# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 08:30:21 2013

@author: daniel
"""

#programa:inversion_2.py
#programa que invierte el orden de una cadena
#variante de inversion_1 
#data input
cadena = raw_input('Introduce una cadena: ')

inversion = ''#inicializa una cadena vacia

for i in range(0, len(cadena)):
    print cadena[i]
    inversion = cadena[i] + inversion
print 'Su inversion es :', inversion
