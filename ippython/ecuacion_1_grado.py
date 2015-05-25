# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 06:45:24 2013

@author: daniel
"""

#programa: ecuacion_1_grado.py
#utilizando <try> and <except>

#data input
a = float(raw_input('Valor de A: '))
b = float(raw_input('Valor de B: '))

#processing and printout
try:
    x = -b/a
    print 'la solucion es %2.4f ' %x
except:
    if b != 0:
        print 'la ecuacion no tiene solucion'
    else:
        print 'la ecuacion tiene infinitas soluciones'
    