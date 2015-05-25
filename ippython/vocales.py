# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 10:51:18 2013

@author: daniel
"""

#programa:vocales.py
#programa que sustituye vocales por puntos 
#ejercicio 194
#data input
cadena = raw_input('Introduce una cadena: ')
nueva_cadena = ''

for caracter in cadena:
    if caracter == 'a' or caracter == 'e' or caracter == 'i' or caracter == 'o' or caracter == 'u':
        caracter = '.'
        nueva_cadena = nueva_cadena + caracter
    else:
        caracter = caracter
        nueva_cadena = nueva_cadena + caracter
print nueva_cadena
        
    
            
