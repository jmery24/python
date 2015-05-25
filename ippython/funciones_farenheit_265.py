# -*- coding: utf-8 -*-
"""
Created on Thu May  9 06:42:06 2013

@author: daniel
"""
#programa: funciones_farenheit_265
#convierte grados celsius a farenheit
#definir funcion de conversion

#definir funcion farenheit
def farenheit(x):
    return (x*9.0/5.0)+32
    
#data input
celsius = float(raw_input('Grados Celsius: '))
print

#invoca o activa funcion
print '%d grados Celsius son %6.2f grados Farenheit' %(celsius, farenheit(celsius))