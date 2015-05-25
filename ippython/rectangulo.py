# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 14:55:19 2012

@author: daniel
"""

#### Calculo del perimetro y area de un rectangulo

## Input data
lado_a = float(raw_input("Longitud del lado A del rectangulo: "))
lado_b = float(raw_input("Longitud del lado B del rectangulo: "))

## Calculo del area y el perimetro
perimetro = lado_a * 2 + lado_b * 2
area = lado_a * lado_b

## Output data
print "El area del rectangulo es :", area, "metros cuadrados"
print "El perimetro del rectangulo es :", perimetro, "metros lineales"
    