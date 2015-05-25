# -*- coding: utf-8 -*-
"""
Created on Fri May 31 06:40:46 2013

@author: daniel
"""

#programa: funciones_cuota-324.py
#calcula la cuota de una hipoteca 'h' por 'n' anios a un interes compuesto
#de 'i' % anual
#ejercicio 324

#define funcion <cuota>
def cuota(h, n, i):
    r = i / (100 * 12)
    m = h * r / (1 - (1 + r) ** (-12 * n))
    return m
    
#cuerpo del programa
#data input
hipoteca = float(raw_input('Valor de la hipoteca: '))
tiempo = int(raw_input('Tiempo en anios de pago: '))
interes = float(raw_input('Valor del Interes: '))

#activa funcion
print
print 'La cuota a pagar es: %2.2f'%(cuota(hipoteca, tiempo, interes))