# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 06:52:44 2013

@author: daniel
"""

#programa: funciones_inversion_351.py
#funcion para invertir una lista, pero la lista original no varia
#ejercicio 351

#definir funcion <invierte>
def invierte(lista):
    c = []
    for i in range(0, len(lista)):
        c.append(lista[len(lista)-1-i])
    return c
        
#cuerpo del programa
#input
a = [1, 2, 3, 4]
b = ['A', 'B', 'C', 'D']

#activa funcion
print 'lista original:  ', a
print 'lista original:  ', b
print
print 'Inversiones'
print 'lista invertida: ', invierte(a)
print 'lista invertida: ', invierte(b)
print
print 'lista original:  ', a
print 'lista original:  ', b