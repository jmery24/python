# -*- coding: utf-8 -*-
"""
Created on Sun May 12 10:29:55 2013

@author: daniel
"""

#programa: funciones_sumatoria.py
#dada una lista definir una funcion que sume todos sus elementos
#tambien probar la funcion predefinida <sum>

#definir funcion <sumatoria>
def sumatoria(lista):
    s = 0
    for numero in lista:
        s += numero
    return s
    
#cuerpo del programa
#data input
num = int(raw_input('Cantidad de elementos en la lista: '))
print

#construye la lista desde el teclado
lista = []
for i in range(num):
    elemento = int(raw_input('Elemento: '))
    lista.append(elemento)

#activa la funcion
print
print 'La sumatoria de la lista', lista, 'es: ', sumatoria(lista)

#sumatoria con funcion predefinida <sum>
print 'la suma total de las lista es: ', sum(lista)