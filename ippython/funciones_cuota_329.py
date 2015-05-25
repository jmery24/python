# -*- coding: utf-8 -*-
"""
Created on Fri May 31 08:16:51 2013

@author: daniel
"""

#programa: funciones_cuota_329.py
#calcula el capital total que pagaremos por una hipoteca 'h' 
#en [10, 15, 20, 25] anios a un interes compuesto de 'i' % anual
#ejercicio 329

#define funcion <cuota>
def cuota(h, n, i):
    r = i / (100 * 12)
    listado = []
    for i in range(len(n)):
        m = (h * r / (1 - (1 + r) ** (-12 * n[i]))) * n[i] * 12
        listado.append(m)
    print listado
    
#cuerpo del programa
#data input
hipoteca = float(raw_input('Valor de la hipoteca: '))
tiempo = [10, 15, 20, 25]
interes = float(raw_input('Valor del Interes: '))

#activa funcion
print
print 'en los siguientes anios: ', tiempo
print 'pagaremos un capital total de: '
cuota(hipoteca, tiempo, interes)