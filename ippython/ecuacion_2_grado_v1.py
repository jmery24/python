# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 06:56:27 2013

@author: daniel
"""

#programa: ecuacion_2_grado_v1.py
#resuelve una ecuacion de 2 grado
#carga modulo sqrt
from math import sqrt

#data input
a  = float(raw_input('Valor de A: '))
b  = float(raw_input('Valor de B: '))
c  = float(raw_input('Valor de C: '))

#processing and printout
try:
    x1 = (-b+sqrt(b**2-4*a*c)/(2*a))
    x2 = (-b-sqrt(b**2-4*a*c)/(2*a))
    if x1 == x2:
        print 'la solucion de la ecuacion es %4.3f' %x1
    else:
        print 'soluciones de la ecuacion: %4.3f, %4.3f' %(x1, x2)
except:
    #no sabemos si el error es divison por cero o raiz cuadrada
    #de un discriminante negativo
    print 'la ecuacion no tiene solucion o es de primer grado'