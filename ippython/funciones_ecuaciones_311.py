# -*- coding: utf-8 -*-
"""
Created on Thu May 30 05:02:00 2013

@author: daniel
"""

#programa: funciones_ecuacion_311
#funcion que reciba los valores de los tres coeficientes
#devuelva: dos soluciones reales 
#None: infinitas soluciones o no so;iciones reales

#importa funcion sqrt
from math import sqrt

#funcion <ecuacion>
def ecuacion(a, b, c):
    if b**2 - 4*a*c >= 0:
        x1 = -b + sqrt((b**2) - (4*a*c)) / 2*a   
        x2 = -b - sqrt((b**2) - (4*a*c)) / 2*a
        return [x1, x2]
    else:
        print
            
#cuerpo principal del programa
#data input
num_1 = int(raw_input('Coeficiente a: '))
num_2 = int(raw_input('Coeficiente b: '))
num_3 = int(raw_input('Coeficiente c: '))
print

#activa funcion <ecuacion>
print 'soluciones: ', ecuacion(num_1, num_2, num_3)
    