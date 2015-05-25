# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 05:26:40 2013

@author: daniel
"""

#programa: funciones_lee_positivos.py
#definir una funcion que lea numeros positivos

#definir funcion lee_entero_positivo
def lee_entero_positivo(texto):
    numero = int(raw_input(texto))
    while numero < 0:
        print 'El numero debe ser entero positivo'
        numero = int(raw_input(texto))
    return numero

#cuerpo del programa

#activa funcion
a = lee_entero_positivo('Escribe un numero entero positivo: ')
b = lee_entero_positivo('Escribe un numero entero positivo: ')
c = lee_entero_positivo('Escribe un numero entero positivo: ')

#output
print
print 'Numeros: ', a, b, c