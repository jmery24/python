# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 18:10:17 2013

@author: daniel
"""

#programa: integral_definida.py
#calcula la integral definida de cualquier funcion
#funcion para calcular la integral de una funcion en un intervalo [a, b]
#con una aproximacion de <n> rectangulos

#definir las funciones

#definir funcion <cuadrado>
def cuadrado(x):
    return x ** 2
#definir funcion <cubo>
def cubo(x):
    return x ** 3
#definir la funcion <integral_x**2>
def integral_indefinida(f, a, b, n):
    if n == 0:
        sumatorio = 0
    else:
        deltax = (b - a) / float(n)
        sumatorio = 0
        for i in range(n):
            sumatorio += deltax * f(a + i * deltax)
    return sumatorio
    
#cuerpo del programa

#input
inicio = float(raw_input('Inicio del Intervalo: '))
final = float(raw_input('Final del Intervalo: '))
partes = int(raw_input('Numero de rectangulos: '))
print

#output y activa funcion
print 'Integracion entre %2.2f y %2.2f' %(inicio, final)
print 'Integral de <x^2>: %2.2f ' % integral_indefinida(cuadrado, inicio, final, partes)
print 'Integral de <x^3>: %2.2f' % integral_indefinida(cubo, inicio, final, partes)