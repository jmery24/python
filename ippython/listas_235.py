# -*- coding: utf-8 -*-
"""
Created on Wed May  1 07:06:20 2013

@author: daniel
"""

#programa: listas_235.py
#remover el elemento de indice <i> de la lista

lista = [1,2,1,5,0,3,8,9]
print 'lista original'
print lista
i = int(raw_input('numero de indice: '))
lista = lista[:i] + lista[i+1:]
print 'misma lista sin el numero correspondiente al indice'
print lista