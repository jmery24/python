# -*- coding: utf-8 -*-
"""
Created on Fri May 31 07:27:14 2013

@author: daniel
"""

#programa: funciones_cuota_325.py
#calcula la cantidad total que pagaremos por una hipoteca 'h' 
#en 'n' anios a un interes compuesto de 'i' % anual
#ejercicio 325

#define funcion <cuota>
def cuota(h, n, i):
    r = i / (100 * 12)
    m = h * r / (1 - (1 + r) ** (-12 * n))
    cantidad = m * 15 * 12
    return cantidad
    
#cuerpo del programa
#data input
hipoteca = float(raw_input('Valor de la hipoteca: '))
tiempo = int(raw_input('Tiempo en anios de pago: '))
interes = float(raw_input('Valor del Interes: '))

#activa funcion
print
print 'Cantidad total a pagar es %2.2f' % (cuota(hipoteca, tiempo, interes))