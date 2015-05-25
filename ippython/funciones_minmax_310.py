# -*- coding: utf-8 -*-
"""
Created on Thu May 30 04:45:54 2013

@author: daniel
"""

#programa: funciones_minmax_310.py
#funcion que devuelve valores multiples mediante una lista
#funcion <minmax> devuelve valor minimo y maximo de una lista
#ejercicio 310

#definir funcion <minmax>
def minmax(listado):
    minimo = min(listado)
    maximo = max(listado)
    return [minimo, maximo]
    
#cuerpo del programa
#data input
numero = int(raw_input('Numero de elementos de la lista: '))
lista = []
for i in range(numero):
    valor = int(raw_input('Numero entero: '))
    lista.append(valor)

#activa la funcion <minmax>
print 'valores minimo y maximo: ', minmax(lista) 