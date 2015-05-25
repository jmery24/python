# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 16:09:38 2013

@author: daniel
"""

#programa: integral.py
#calcula la integral definida de f(x) = X^2
#funcion para calcular la integral de x**2 en un intervalo [a, b]
#con una aproximacion de <n> rectangulos

#definir la funcion <integral_x**2>
def integral_x2(a, b, n):
    if n == 0:
        sumatorio = 0
    else:
        deltax = (b - a) / float(n)
        sumatorio = 0
        for i in range(n):
            sumatorio += deltax * (a + i * deltax) ** 2
    return sumatorio
    
#cuerpo del programa

#input
inicio = float(raw_input('Inicio del Intervalo: '))
final = float(raw_input('Final del Intervalo: '))
partes = int(raw_input('Numero de rectangulos: '))
print

#output y activa funcion
print 'La integral de <x^2> entre %2.2f y %2.2f' %(inicio, final)
print 'vale aproximadamente %2.2f' % integral_x2(inicio, final, partes)