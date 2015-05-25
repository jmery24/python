# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 05:23:54 2013

@author: daniel
"""

#programa: funciones_inversion.py
#procedimiento para invertir una lista

#definir funcion <invierte>
def invierte(lista):
    for i in range(len(lista)/2):
        c = lista[i]
        lista[i] = lista[len(lista) - 1 - i]
        lista[len(lista) - 1 - i] = c
        
#cuerpo del programa
#input
a = [1, 2, 3, 4, 5]
b = ['A', 'B', 'C', 'D']

#activa funcion
print 'lista original:  ', a
print 'lista original:  ', b
print
print 'Inversiones'
invierte(a)
print 'lista invertida: ', a
invierte(b)
print 'lista invertida: ', b

        