# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 10:03:36 2013

@author: daniel
"""

#programa:palindromo_1.py
#programa que verifica ri una palabra y su inversion coinciden 
#variante de palindromo.py
#ejercicio 191
#data input
cadena = raw_input('Introduce una cadena: ')

inversion = ''#inicializa una cadena vacia

for caracter in cadena:
    inversion = caracter + inversion
    
print 'Su inversion es :', inversion
if cadena == inversion:
    print 'es una palabra palindromo'
else:
    print 'la palabra y su inversion no coinciden'