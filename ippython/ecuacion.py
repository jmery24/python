# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 07:50:31 2013

@author: daniel
"""

# Programa: ecuacion.py
# Proposito:  calcula x partiendo de los datos a y b
# Autor: Daniel Mery
# Fecha: 02/10/2013

# Math Module:

# Data input: valores de a y b
valor_a = float(raw_input("Escribe el valor de a: "))
valor_b = float(raw_input("Escribe el valor de b: "))

# data computation: calcula el valor de x y analiza valor de a
if valor_a != 0:
    if valor_b != 0:
        resultado = -valor_b/valor_a
        print "El valor de x es de %6.2f" % resultado #muestra 2 decimales
    if valor_b == 0:
        print "La ecuacion tiene infinitas soluciones"    
else:
    if valor_b != 0:
        print "La ecuacion no tiene solucion"
    if valor_b == 0:
        print "La ecuacion tiene infinitas soluciones"
    
# end program
print "Gracias por utilizar esta aplicacion"



