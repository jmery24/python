# -*- coding: utf-8 -*-
"""
Created on Tue May 21 17:43:33 2013

@author: daniel
"""

#programa: pagina_242.py
#definir funciones para calcular la distancia al origen

#importa funcion sqrt
from math import sqrt

#define funciones
#funcion cuadrado
def cuadrado(x):
    return x ** 2
    
#funcion suma-cuadrados
def suma_cuadrados(v):
    s = 0
    for e in v:
        s += cuadrado(e)
    return s
    
#programa principal

#data input
vector = []
for i in range(3):
    vector.append(float(raw_input('Dame un numero: ')))

#activa funciones
y = suma_cuadrados(vector)

#data output
print 'distancia al origen: ', sqrt(y)