# -*- coding: utf-8 -*-
"""
Created on Fri May 31 07:37:37 2013

@author: daniel
"""

#programa: funciones_cuota_327.py
#calcula el porcentaje del capital pagaremos por una hipoteca 'h' 
#en 'n' anios a un interes compuesto de 'i' % anual
#ejercicio 327

#define funcion <cuota>
def cuota(h, n, i):
    r = i / (100 * 12)
    m = h * r / (1 - (1 + r) ** (-12 * n))
    cantidad = m * 15 * 12
    interes = cantidad - h
    porcentaje = (interes * 100) / h
    return porcentaje
    
#cuerpo del programa
#data input
hipoteca = float(raw_input('Valor de la hipoteca: '))
tiempo = int(raw_input('Tiempo <en anios> para pagar: '))
interes = float(raw_input('Valor del Interes: '))

#activa funcion
print
print 'Porcentaje del capital a pagar en interes:  %2.2f' % (cuota(hipoteca, tiempo, interes))