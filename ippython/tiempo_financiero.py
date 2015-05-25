# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 07:19:42 2013

@author: daniel
"""

#programa: tiempo_financiero.py
#calcula el tiempo necesario para obtener un capital (Cf) partiendo de una inversion inicial (Ci) a una tasa anual de interes (interes)

#importar funcion logaritmo de modulo math
from math import log

#data input
Ci = float(raw_input('Capital inicial invertido: '))
Cf = float(raw_input('Capital final obtenido: '))
interes = float(raw_input('Tasa de interes anual: '))

#data computation
if Cf < Ci or interes <= 0:
    print "no es posible la operacion financiera"
else:
    if Cf == Ci:
        print 'La operacion financiera no tiene sentido'
    else:
        tiempo = ((log(Cf)-log(Ci))/log(1+interes/100))
        print 'El tiempo es de %2.4f anios' %tiempo