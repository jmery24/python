# -*- coding: utf-8 -*-
"""
Created on Wed May  1 06:52:57 2013

@author: daniel
"""

#programa: listas_234.py
#remover los elementos pares de una lista

lista = [1,2,1,5,0,3,8,9]
print 'lista original'
print lista
i = 0
while i < len(lista):
    print i
    if lista[i] % 2 == 0:
        del lista[i]
    else:
        i += 1
print 'misma lista sin numeros pares'
print lista