# -*- coding: utf-8 -*-
"""
Created on Tue May 14 06:43:46 2013

@author: daniel
"""

#programa: funciones_series_279.py
#dada una lista calcular la cantidad de numeros repetidos contiguos
#crear una funcion que realice dicho calculo

#funcion <series>
def series(lista):
    suma = 0
    for i in range(0, len(lista)):
        if lista[i] != lista[i-1]:
            suma += 1
        if suma == 0:
            suma = 1
    return suma
    
#cuerpo del programa
#data input
num = int(raw_input('Cantidad de elementos en la lista: '))
print

#crea una lista
listado = []
for i in range(num):
    elemento = int(raw_input('Elemento: '))
    listado.append(elemento)
    
#activa funcion
#activa la funcion
print
print 'El numero de series de la lista', listado, 'es: ', series(listado)
print