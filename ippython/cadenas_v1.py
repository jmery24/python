# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 07:53:21 2013

@author: daniel
"""

#programa:cadenas_v1.py
#ejercicios 157 y 158

#data input
cadena = raw_input('Escribe palabras: ')

#processing and printout
for caracter in cadena:
    print caracter
print ' '    
    
#variante de for in; muestra <palabra> menos el ultimo caracter
for i in range(len(cadena)-1):
    print i, cadena[i]
print ' '
    
#variante de for in; muestra <palabra> invertida
for i in range(len(cadena)-1,-1,-1):
    print i, cadena[i]