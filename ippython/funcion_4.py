# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 07:54:24 2013

@author: daniel
"""

def sumar(x, y):
    return x + y
    
def multiple(x, y):
    return x + y, x * y

num_1 = int(raw_input('Valor de un numero: '))
num_2 = int(raw_input('Valor de otro numero: '))
a = int(raw_input('Valor de A: '))
b = int(raw_input('Valor de B: '))

print sumar(num_1, num_2)
print multiple(num_1, num_2) 
print sumar(6, 6)
print multiple(6 ,6)
print sumar(a, b)
print multiple(a, b)