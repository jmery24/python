# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 07:29:55 2013

@author: daniel
"""

#programa:numero_primo.py
#verifica si un numero dado es numero primo

#data input
num = int(raw_input('Introduce un numero entero: '))

#proccesing and printout
for divisor in range(2, num):
    print '%d dividido %d' %(num, divisor),
    print 'es %d con resto %d' %(num/divisor, num%divisor)
    