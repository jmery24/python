# -*- coding: utf-8 -*-
"""
Created on Fri May  3 07:21:50 2013

@author: daniel
"""

#programa: split_240.py
# en <texto> escribir varias frases y contarlas
#ejercicios: 241 y 242

texto = raw_input('Escribe varias frases: ')
lista = texto.split('.')
del lista[len(lista)-1]
print lista
print 'Cantidad de frases: ', len(lista)

for i in range(0, len(lista)):
    elemento = lista[i]
    print 'Cantidad de palabras: ', len(elemento.split())
print 'Gracias por utilizar el programa'
    