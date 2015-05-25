# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 07:08:51 2013

@author: daniel
"""

# Programa: circulo.py
# Proposito:  calcula el area y el perimetro de un circulo conociendo su radio
# Autor: Daniel Mery
# Fecha: 02/09/2013

# Math Module: carga funcion pi
from math import pi

# Data input: valor del radio (en metros)
radio = float(raw_input("Escribe el valor del radio: "))

# data computation: calcula el perimetro y el area del circulo
area = pi*radio**2
perimetro = pi*radio*2

# data output: muestra en pantalla el valor del area y perimetro
print "El area del circulo es de %6.3f metros cuadrados" % area #muestra 3 decimales
print "El perimetro del circulo es de %6.3f metros" % perimetro #muestra 3 decimales