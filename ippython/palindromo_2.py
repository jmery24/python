# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 10:15:14 2013

@author: daniel
"""

#programa:palindromo_2.py
#programa que verifica si una frase es igual a su inversion
#ejercicio 192
#data input
cadena = raw_input('Introduce una cadena: ')
cadena_1 = ''
inversion = ''#inicializa una cadena vacia

for i in range(0, len(cadena)):
    if cadena[i] != ' ':
        cadena_1 += cadena[i] 
        inversion = cadena[i] + inversion
    else:
        print 'next'
if cadena_1 == inversion:
    print 'es una frase palindromo'
else:
    print 'la frase y su inversion no coinciden'