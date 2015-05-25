# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 05:33:52 2013

@author: daniel
"""

# calcula volumen de una esfera

# modulo math
from math import pi

# radio input
radio = float(raw_input("radio: "))

# calcula volumen
volumen = 4.0/3.0 * pi * radio ** 3

# data output
print("volumen de la esfera= "), volumen
