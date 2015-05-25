# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 17:40:37 2012

@author: daniel
"""

#### Calculo del volumen de una esfera

from math import pi

#### data input
radio = float(raw_input("Valor del radio: "))

### calculo de la esfera
volumen = 4.0 / 3.0 * pi * radio **3

##### data output
print "El volumen es: ", volumen
print "Gracias por usar este programa"

