# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 07:13:41 2013

@author: daniel
"""

#programa: ecuacion_2_grado_v2.py
#resuelve una ecuacion de 2 grado y discrimina tipo de error de
#ejecucion
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
except ZeroDivisionError:
    if b != 0:
        print 'la ecuacion no tiene solucion'
    else:
        print 'la ecuacion tiene infinitas soluciones'
except ValueError:
    print 'no hay soluciones reales'
    