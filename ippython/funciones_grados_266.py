# -*- coding: utf-8 -*-
"""
Created on Thu May  9 07:08:51 2013

@author: daniel
"""

#programa: funciones_grados_266
#convierte radianes a grados
#definir funcion de conversion

#importar de Math el valor pi
from math import pi

#definir funcion grados
def grados(x):
    return (x*180.0)/pi
    
#data input
radianes = float(raw_input('Radianes: '))
print

#invoca o activa funcion
print '%0.2f radianes son %6.2f grados' %(radianes, grados(radianes))