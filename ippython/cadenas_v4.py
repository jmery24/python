# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 08:31:24 2013

@author: daniel
"""

#programa:cadenas_v4.py
#calcula la cantidad de palabras en base a los espacios en blanco


#data input
cadena = raw_input('Escribe una frase: ')

#inicializacion de variable
cantidad = 0
anterior = ' '

#processing
#calcula la cantidad de espacios en blanco en la cadena

for i in cadena:
    if i == ' ' and anterior != ' ' :
        cantidad +=1
    anterior = i
if cadena[-1] == ' ':
    cantidad -= 1
        
#printout la cantidad de palabras        
print 'Hay %d palabra(s) en la frase' % (cantidad+1)