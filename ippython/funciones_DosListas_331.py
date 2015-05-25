# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 05:28:04 2013

@author: daniel
"""

#programa: funciones_DosListas_331.py
#se comparan dos listas
#la funcion devuelve una lista sin elementos repetidos y 
#que pertenezcan a ambas listas 
#<UNION DE CONJUNTOS>
#ejercicio 331

#definir la funcion <no_repetidos>
def no_repetidos(lista, listado):
    resultado = []
    for elemento in lista:
        if elemento not in resultado:
            resultado.append(elemento)
        for elemento in listado:
            if elemento in listado:
                if elemento not in resultado:
                    resultado.append(elemento)
    return resultado
    
#cuerpo del programa
#data input
lista_1 = []
cantidad = int(raw_input('Cantidad de elementos de la lista A: '))
for i in range (0, cantidad):
    elemento = int(raw_input('Escribe un elemento: '))
    lista_1.append(elemento)
    
lista_2 = []
cantidad = int(raw_input('Cantidad de elementos de la lista B: '))
for i in range (0, cantidad):
    elemento = int(raw_input('Escribe un elemento: '))
    lista_2.append(elemento)
    
    
#activa la funcion
print
print 'listados originales'
print lista_1
print lista_2
print
print 'lista con elementos en ambas listas y no repetidos'
print no_repetidos(lista_1, lista_2)