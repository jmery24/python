# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 06:06:14 2013

@author: daniel
"""

#programa: funciones_factorial.py
#mostramos mostramos la version 'recursiva' y la 'iterativa'

#definimos la funcion <factorial_recursivo>, metodo recursivo
def factorial_recursivo(n):
    if n == 0 or n == 1:
        resultado = 1
    elif n > 1:
        resultado = n * factorial_recursivo(n -1)
    return resultado
    
#definimos la funcion <factorial_iterativo>, metodo iterativo
def factorial_iterativo(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f
    
#cuerpo de programa
#input
numero = int(raw_input('Escribe un numero: '))

#activa funcion
print
print 'El factorial de  <recursivo> ', numero, 'es: ', factorial_recursivo(numero)
print
print
print 'El factorial de <iterativo> ', numero, 'es: ', factorial_iterativo(numero)
print