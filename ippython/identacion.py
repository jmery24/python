# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 06:25:50 2013

@author: daniel
"""

#programa:identacion.py
#el programa comprueba si un numero entero dado es par on impar

#data input
num = int(raw_input('escribe un numero entero positivo :'))

#processing and printout
while num < 0:
    num = int(raw_input('un numero positivo :'))
if num % 2 == 0:
    print 'numero par'
else:
    print 'numero impar'
    