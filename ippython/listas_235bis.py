# -*- coding: utf-8 -*-
"""
Created on Wed May  1 07:14:37 2013

@author: daniel
"""
#programa: listas_235bis.py
#realiza la misma tarea que el programa listas_235.py

lista = [1,2,1,5,0,3,8,9]
print 'lista original'
print lista
j = int(raw_input('numero de indice: '))
i = 0
while i < len(lista):
    print i
    if i == j:
        del lista[i]
        i += 1
    else:
        i += 1
print 'misma lista sin el numero de la lista indicado'
print lista
