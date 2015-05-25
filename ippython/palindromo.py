# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 09:58:06 2013

@author: daniel
"""

#programa:palindromo.py
#programa que verifica si una cadena es igual a su inversion
#ejercicio 191
#data input
cadena = raw_input('Introduce una cadena: ')

inversion = ''#inicializa una cadena vacia

for i in range(0, len(cadena)):
    inversion = cadena[i] + inversion
print 'Su inversion es :', inversion
if cadena == inversion:
    print 'es una palabra palindromo'
else:
    print 'cadena y su inversion no coinciden'