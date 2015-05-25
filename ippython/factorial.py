# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 07:35:08 2013

@author: daniel
"""

#programa: factorial.py
#calcula el factorial de un numero

#data input
num = int(raw_input('Calcula el factorial de numero natural: '))
i = 1
factorial = 1

#processing data
while i <= num:
    factorial *= i
    i += 1
    
#printout    
print 'El factorial del ', num, 'es igual a ', factorial
print 'El factorial del numero %d es igual a %d' %(num, factorial)