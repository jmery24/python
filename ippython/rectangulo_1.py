# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 08:06:05 2013

@author: daniel
"""

# perimetro y area de un rectangulo

# introduce valos de los lados
ancho = float(raw_input("ancho: "))
largo = float(raw_input("largo: "))

# calculo del perimetro y el area
perimetro = 2*(ancho+largo)
area = ancho*largo

# output data
print("perimetro= "), perimetro
print("area: "), area
