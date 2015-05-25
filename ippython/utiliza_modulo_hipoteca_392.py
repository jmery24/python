# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 17:43:23 2013

@author: daniel
"""

#programa: utiliza_modulo_hipoteca_392.py
#este programa importa tres funciones del modulo hipoteca
#ejercicio 392
#invoca el modulo
from hipoteca import *

#cuerpo del programa

#data input
eleccion = menu()
if eleccion == 'a':
    print
    hipoteca = float(raw_input('Valor de la hipoteca: '))
    tiempo = int(raw_input('Tiempo <en anios> para pagar: '))
    interes = float(raw_input('Valor del Interes: '))
    print 'La cuota a pagar es: %2.2f'%(cuota(hipoteca, tiempo, interes))
elif eleccion == 'b':
    print
    hipoteca = float(raw_input('Valor de la hipoteca: '))
    tiempo = int(raw_input('Tiempo <en anios> para pagar: '))
    interes = float(raw_input('Valor del Interes: '))
    print 'Porcentaje del capital a pagar en interes:  %2.2f' % (porciento(hipoteca, tiempo, interes))
elif eleccion == 'c':
    print 
    print 'Gracias por utilizar el programa'
else:
    print
    print 'opcion no valida'