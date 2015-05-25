# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 07:14:58 2013

@author: daniel
"""

#programa: listas_233.py
#remover los elementos de indice par en una lista

lista = [1,2,1,5,0,3,8,9]
print 'lista original'
print lista
i = 0
while i < len(lista):
    print lista[i]
    del lista[i]
    i += 1
print 'misma lista sin indices pares'
print lista