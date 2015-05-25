# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 05:05:45 2013

@author: daniel
"""

#programa: funciones_no_repetido.py
#la funcion devuelve una lista sin elementos repetidos

#definir la funcion <sin_repetidos>
def sin_repetidos(lista):
    resultado = []
    for elemento in lista:
        if elemento not in resultado:
            resultado.append(elemento)
    return resultado
    
#cuerpo del programa
#data input
listado = []
cantidad = int(raw_input('Cantidad de elementos de la lista: '))
for i in range (0, cantidad):
    elemento = int(raw_input('Escribe un elemento: '))
    listado.append(elemento)
    
#activa la funcion
print
print 'listado original'
print listado
print
print 'nueva lista sin elementos repetidos'
print sin_repetidos(listado)