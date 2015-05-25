# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 07:44:06 2013

@author: daniel
"""

#programa: funciones_concatena_inversion_353.py
#funcion para concatenar una lista con su inversion 
#la lista original no varia
#ejercicio 353

#definir funcion <concatena_invierte>
def concatena_invierte(lista):
    c = []
    for i in range(0, len(lista)):
        c.append(lista[len(lista)-1-i])
    c = lista + c
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
print 'lista invertida: ', concatena_invierte(a)
print 'lista invertida: ', concatena_invierte(b)
print
print 'lista original:  ', a
print 'lista original:  ', b