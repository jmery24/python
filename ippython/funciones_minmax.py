# -*- coding: utf-8 -*-
"""
Created on Wed May 29 08:19:56 2013

@author: daniel
"""

#programa: funciones_minmax.py
#funcion que devuelve valores multiples mediante una lista
#funcion <minmax> devuelve valor minimo y maximo de una lista

#definir funcion <minmax>
def minmax(a, b, c):
    minimo = min(a, b, c)
    maximo = max(a, b, c)
    return [minimo, maximo]
    
#cuerpo del programa
#data input
valor_1 = int(raw_input('El valor de A: '))
valor_2 = int(raw_input('El valor de B: '))
valor_3 = int(raw_input('El valor de C: '))

#activa la funcion <minmax>
print 'valores minimo y maximo: ', minmax(valor_1, valor_2, valor_3) 