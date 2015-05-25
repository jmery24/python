# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 08:12:21 2013

@author: daniel
"""

#programa:cadenas_v2.py
#ejercicio 159-160 escribir una cadena y que muestre el numero 
#de espacios en blanco que contiene

#data input
cadena = raw_input('Escribe una cadena: ')

#inicializacion de variables
cantidad = 0
mayusculas = 0

#processing
#calcula la cantidad de espacios en blanco en la cadena
for i in range(len(cadena)):
    if cadena[i] == ' ':
        cantidad +=1
#calcula la cantidad de letras mayusculas en la cadena        
for i in range(len(cadena)):
    if cadena[i] >= 'A' and cadena[i] <= 'Z':
        mayusculas +=1
        
#printout        
print 'Hay %d espacios en blanco en la cadena' % cantidad
print 'Hay %d mayusculas en la cadena' % mayusculas    