# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 18:44:11 2013

@author: daniel
"""
from math import cos

#definir funcion <coseno>
def coseno(x):
    return cos(x) 

#definir la funcion <integral_x**2>
def integral_indefinida(f, alfa, beta):
    sumatorio = 0
    for i in range(0, 90):
        sumatorio += cos(i)
    return sumatorio
    
#cuerpo del programa

#input
inicial = float(raw_input('Angulo inicial: '))
final = float(raw_input('Angulo final: '))

#output y activa funcion
print 'La integral es: ', integral_indefinida(coseno, inicial, final)