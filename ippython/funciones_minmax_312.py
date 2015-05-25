# -*- coding: utf-8 -*-
"""
Created on Thu May 30 06:14:10 2013

@author: daniel
"""

#programa: funciones_minmax_312
#funcion que recibe una cadena de palabras
#devuelve la 1ra y ultima palabra por orden alfabetico
#ejercicio 312

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
    palabra = raw_input('Palabra: ')
    lista.append(palabra)

#activa la funcion <minmax>
print 'primera y ultima palabra: ', minmax(lista) 