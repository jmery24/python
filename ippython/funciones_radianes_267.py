# -*- coding: utf-8 -*-
"""
Created on Thu May  9 07:37:29 2013

@author: daniel
"""

#programa: funciones_radianes_267
#convierte grados a radianes
#definir funcion de conversion

#importar de Math el valor pi
from math import pi

#definir funcion radianes
def radianes(x):
    return (x*pi)/180
    
#data input
grados = float(raw_input('Grados: '))
print

#invoca o activa funcion
print '%0.2f grados son %6.2f radianes' %(grados, radianes(grados))