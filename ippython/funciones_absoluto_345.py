# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 05:46:19 2013

@author: daniel
"""

#programa: funciones_absoluto_345.py
#procedimiento devuelve el valor absoluto de una lista
#ejercicio 345

#definir procedimiento <absoluto>
def absoluto(lista):
    for i in range(len(lista)):
        lista[i] = abs(lista[i])
        
#cuerpo del programa
#input
mi_lista = [1, -1, 2, -3, -2, 0]

#activa procedimiento
print 'lista original: ', mi_lista
absoluto(mi_lista)
print 'nueva lista:    ', mi_lista