# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 12:55:14 2012

@author: daniel
"""

#### Circle program: get radius and compute area and perimeter

#### impor pi value from math module
from math import pi

#### input data: radius
radio = float(raw_input("Radio= "))

#### compute the area and perimeter
area = pi * radio ** 2
longitud = pi * 2 * radio

#### printout area and perimeter
print "El area de la circunferencia es %2.4f metros cuadrados" % area
print "El perimetro de la circunferencia es %2.4f metros" % longitud

 
