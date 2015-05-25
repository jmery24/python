# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 05:40:10 2013

@author: daniel
"""

#programa: funciones_inversion_344.py
#procedimiento para invertir una lista
#ejercicio 344

#definir funcion <invierte>
def invierte(lista):
    for i in range(len(lista)/2):
        c = lista[i]
        lista[i] = lista[-i - 1]
        lista[-i - 1] = c
        
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