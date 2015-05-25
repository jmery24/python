# -*- coding: utf-8 -*-
"""
Created on Wed May 22 07:00:02 2013

@author: daniel
"""

#programa: funciones_ecuacion_292.py
#la funcion calcula la solucion a una ecuacion lineal ax+b=0
#dados los valores (a, b)
#infinitas soluciones  o no solucion = none

#definir la funcion <ecuacion>
def ecuacion(a,b):
    if a == 0 or b == 0:
        return None
    else:
        x = -b/a
    return x
        
#cuerpo del programa
#data input
valor_a = float(raw_input('Valor del numero A: '))
valor_b = float(raw_input('Valor del numero B: '))

#activa funcion
print
print 'la solucion de la ecuacion es: ', ecuacion(valor_a, valor_b)   