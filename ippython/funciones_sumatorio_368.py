# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 06:37:38 2013

@author: daniel
"""

#programa: funciones_sumatoria_368.py
#definir una funcion sumatoria recursiva
#ejercicio 368

#definir la funcion recursiva <sumatorio_recursivo>
def sumatorio_recursivo(n):
    if n == 1:
        resultado = 1
    if n > 1:
        resultado = n + sumatorio_recursivo(n-1)
    return resultado
    
#definir funcion <sumatorio_iterativo>
def sumatorio_iterativo(n):
    resultado = 1
    for i in  range(2, n+1):
        resultado += i
    return resultado

#cuerpo del programa

#input
numero = int(raw_input('Escribe un numero: '))

#activa la funcion
print
print 'Sumatoria <recursiva> de ', numero, 'es: ', sumatorio_recursivo(numero)
print
print
print 'Sumatoria <iterativa> de ', numero, 'es: ', sumatorio_iterativo(numero)
print