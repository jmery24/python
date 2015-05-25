# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 07:38:54 2013

@author: daniel
"""

def f(x, y):
    x += 3
    y.append(28)
    print x, y#x asume el valor x+3, dentro de la funcion
    
x = 22
y = [26]


f(x, y)
print x, y#x es un entero no mutable, no conserva el valor de la funcion