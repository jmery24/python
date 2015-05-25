# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 19:47:17 2012

@author: daniel
"""

# Ejercicio 60
# Data input
persona_a = raw_input("Edad de persona <a>")
persona_b = raw_input("Edad de persona <b>")

#Estructura de control, calculo y printout
if persona_a != persona_b:
    if persona_a > persona_b:
        print "persona <a> es mayor que persona <b>"
    if persona_a < persona_b:
        print "persona <a> es menor que persona <b>"
        
if persona_a == persona_b:
    print " Tienen la misma edad"
    
    
