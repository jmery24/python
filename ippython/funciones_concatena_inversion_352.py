# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 07:52:02 2013

@author: daniel
"""

#programa: funciones_concatena_inversion_352.py
#funcion para concatenar una lista con su inversion 
#devuelve una copia, la lista original es modificada (REVISAR)
#ejercicio 352

#definir funcion <concatena_invierte>
def concatena_invierte(lista):
    c = []
    for i in range(0, len(lista)):
        c.append(lista[len(lista)-1-i])
    lista = lista + c    
    return lista
        
#cuerpo del programa
#input
a = [1, 2, 3, 4]
b = ['A', 'B', 'C', 'D']

#activa funcion
print 'lista original:  ', a
print 'lista original:  ', b
print
print 'Inversiones'
print 'lista concatenada con invertida: ', concatena_invierte(a)
print 'lista concatenada con invertida: ', concatena_invierte(b)
print
print 'lista original:  ', a
print 'lista original:  ', b