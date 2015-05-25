# -*- coding: utf-8 -*-
"""
Created on Fri May 31 07:32:39 2013

@author: daniel
"""

#programa: funciones_cuota_326.py
#calcula el interes que pagaremos por una hipoteca 'h' 
#en 'n' anios a un interes compuesto de 'i' % anual
#ejercicio 326

#define funcion <cuota>
def cuota(h, n, i):
    r = i / (100 * 12)
    m = h * r / (1 - (1 + r) ** (-12 * n))
    cantidad = m * 15 * 12
    interes = cantidad -h
    return interes
    
#cuerpo del programa
#data input
hipoteca = float(raw_input('Valor de la hipoteca: '))
tiempo = int(raw_input('Tiempo en anios de page: '))
interes = float(raw_input('Valor del Interes: '))

#activa funcion
print
print 'Interes a pagar es %2.2f' % (cuota(hipoteca, tiempo, interes))