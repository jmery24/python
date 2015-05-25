# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 19:12:26 2012

@author: daniel
"""

### Programa: primer_grado_84.py
### Calcula ecuaciones de primer grado
###Estrucura de Control, Sentencia Condicional

# Data Input
a = float(raw_input("Valor de <a>: "))
b = float(raw_input("Valor de <b>: "))

# Calculo, sentencia condicional y printout
if a != 0:
    x = -b/a
    print "el valor de x es igual a ", x

if a == 0:
    print "La ecuacion no tiene solucion, x es un valor indeterminado"
    
    

