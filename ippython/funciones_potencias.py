# -*- coding: utf-8 -*-
"""
Created on Wed May  8 06:52:52 2013

@author: daniel
"""

#programa: funciones_potencias.py
#en este programa definiremos una funcion y la invocaremos o activaremos

#definir la funcion de nombre <cuadrado>
def cuadrado(x):
    return x ** 2
    
#definir la funcion <cubo>
def cubo(x):
    return x ** 3

#data input
argumento = int(raw_input('Numero entero: '))
print

#invocamos o activamos la funcion
print 'Valor de %d**2 es %d' %(argumento, cuadrado(argumento))
print
print 'Valor de %d**3 es %d' %(argumento, cubo(argumento))
print

a = cuadrado(3)
print 'Valor de 3**2 es', a
print
print 'Valor de 2**2 es', cuadrado(2)