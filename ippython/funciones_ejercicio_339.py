# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 05:07:15 2013

@author: daniel
"""

#programa: funciones_ejercicio_339.py
#definir una funcion que modifica dos listas
#input: dos listas
#ejercicio 339

#definir la funcion <modifica>
def modifica(a, b):
    for elemento in b:
        a.append(elemento)
    b = b + [4]
    a[-1] = 100
    del b[0]
    return b[:]
    
#cuerpo del programa
#data input
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]

#activa funcion
lista3 = modifica(lista1, lista2)

#output
print 'lista 1: ', lista1 #ver nota al pie
print 'lista 2: ', lista2
print
print 'lista 3: ', lista3
#operaciones como <append>, <del> o la asignacion a elementos indexados de
#listas modifican a la propia lista, entonces los cambios afectan al
#parametro y el argumento