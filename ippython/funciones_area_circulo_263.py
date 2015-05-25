# -*- coding: utf-8 -*-
"""
Created on Wed May  8 07:51:22 2013

@author: daniel
"""

#programa: funciones_area_circulo_263.py
#definir una funcion para calcular el area de un circulo

#importar funcion pi
from math import pi

#definir la funcion
def area(x):
    return pi * (x ** 2.0)
    
#data input
radio = float(raw_input('Valor del radio: '))
print

#invoca la funcion
print 'El area de circulo de radio %f es %f' %(radio, area(radio))



