# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 12:06:30 2012

@author: daniel
"""
#### Claculo del perimetro y el area de un cuadrado

#### Data input
lado = float(raw_input("Introduzca la longitud del lado de un cuadrado: "))

#### Calculo del area y perimetro
area = lado * lado
perimetro = lado * 4

#### Data output
print "Para un cuadrado de", lado, "metros por cada lado"
print "Tenemos una superficie =", area, "metros cuadrados"
print "y un perimetro =", perimetro, "metros lineales"