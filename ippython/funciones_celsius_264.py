# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:05:35 2013

@author: daniel
"""

#programa: funciones_celsius_264
#convierte grados farenheit a celsius
#definir funcion de conversion

#definir funcion celsius
def celsius(x):
    return (x - 32) * 5.0/9.0
    
#data input
farenheit = float(raw_input('Grados Farenheit: '))
print

#invoca o activa funcion
print '%d grados Farenheit son %6.2f grados Celsius' %(farenheit, celsius(farenheit))