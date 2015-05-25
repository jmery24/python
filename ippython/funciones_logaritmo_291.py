# -*- coding: utf-8 -*-
"""
Created on Wed May 22 06:27:11 2013

@author: daniel
"""

#programa: funciones_logaritmo_291
#funcion para calcular el valor logaritmico de un numero <x> en base <b>

#importar funcion logaritmica
from math import log

#definir funcion <logaritmo>
def logaritmo(x,b):
    return log(x,b)
    
#cuerpo del programa
#data input
base = float(raw_input('base logaritmica: ' ))
numero = float(raw_input('numero: '))

#activa funcion <logaritmo>
print 'el logaritmo de %f en base %f es: %f ' %(numero, base, logaritmo(numero, base))
print 'logaritmo de %f en base 10 es %f: ' % (numero, log(numero, base))