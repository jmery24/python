# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 07:36:10 2013

@author: daniel
"""

#programa: listas_231.py
#no funciona

lista = []
cadena = raw_input('escribe una cadena: ')
lista = cadena.split()
print lista
for i in range(0, len(cadena)):
#    print cadena[i]
    if cadena[i] != '':
        elemento = cadena[i]
#        print elemento
        lista.append(elemento)
    else:
        print 'no considera espacio en blanco'
print lista
        