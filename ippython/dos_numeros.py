# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 07:19:01 2013

@author: daniel
"""

#data input
numero_a = int(raw_input('numero entero A: '))
numero_b = int(raw_input('numero entero B: '))

#procesing
if numero_b == numero_a**2:
    print 'el numero B es igual al cuadrado del numero A' 
else:
    if numero_b > numero_a**2:
        print 'el numero B es mayor que el cuadrado del numero A'
    else:
        print 'el numero B es menor que el cuadrado del numero A'
        