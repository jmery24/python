# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 07:43:35 2013

@author: daniel
"""

#programa: cadenas.py
#dada una palabra la escribe letra x letra

#data input
palabra = raw_input('Escribe palabras: ')

#processing and printout
for caracter in palabra:
    print caracter
    
#variante de for in 
for i in range(len(palabra)):
    print i, palabra[i]
    
# variante para escribir la palabra en forma inversa
for i in range(len(palabra)):
    print i, palabra[len(palabra)-i-1]
    