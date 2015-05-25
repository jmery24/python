# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 06:58:06 2013

@author: daniel
"""

#programa: funciones_sumatoria_369.py
#definir una funcion sumatoria recursiva para <n> y <i=m>
#definir una funcion sumatoria iterativa para <n> y <i=m>
#ejercicio 369

#definir la funcion recursiva <sumatorio_recursivo>
def sumatorio_recursivo(n, m):
    if n < m:
        return None
    if n == m:
        resultado = m
    if n > m:
        resultado = n + sumatorio_recursivo(n-1, m)
    return resultado
    
#definir funcion <sumatorio_iterativo>
def sumatorio_iterativo(n, m):
    resultado = 0
    for i in  range(m, n+1): 
        resultado += i
    return resultado

#cuerpo del programa

#input
numero_a = int(raw_input('Escribe un numero: '))
numero_b = int(raw_input('Escribe un numero: '))

#activa la funcion
print
print 'Sumatoria <recursiva> de ', numero_b, numero_a, 'es: ', sumatorio_recursivo(numero_a, numero_b)
print
print
print 'Sumatoria <iterativa> de ', numero_b, numero_a, 'es: ', sumatorio_iterativo(numero_a, numero_b)
print