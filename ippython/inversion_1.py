# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 08:19:48 2013

@author: daniel
"""

#programa:inversion.py
#programa que invierte el orden de una cadena 
#data input
cadena = raw_input('Introduce una cadena: ')

inversion = ''#inicializa una cadena vacia

for caracter in cadena:
    print caracter
    inversion = caracter + inversion
print 'Su inversion es :', inversion

