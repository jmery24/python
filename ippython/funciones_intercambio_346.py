# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 05:56:30 2013

@author: daniel
"""

#programa: funciones_intercambio_346.py
#procedimiento para intercambiar los vlores de dos listas
#ejercicio 346

#definir procedimiento <intercambio>
def intercambio(lista1, lista2):
    auxiliar = lista1
    lista1 = lista2
    lista2 = auxiliar
    return lista1, lista2
    
#cuerpo del programa
#input
a = [1, 2]
b = [3, 4, 5]

#activa procedimiento
print 'listados originales A y B: ', a, b
print
print ' listados intercambiados A y B: ', intercambio(a, b)