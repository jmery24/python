# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 06:42:39 2013

@author: daniel
"""

#programa: listas_borrado.py
#para remover elementos de una lista utilizamos <del>
#<del> como <append>, solo actua sobre la lista que opera, o sea
#la modifica 

lista = [1,2,-3,-4,5,-6]
print 'lista original'
print lista
i = 0
while i < len(lista):
    print i
    if lista[i] < 0:
        del lista[i]
    else:
        i += 1
print 'misma lista sin numeros negativos'
print lista