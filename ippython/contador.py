# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 06:29:32 2013

@author: daniel
"""

#programa:contador.py
#utiliza while para realizar un bucle
#data input
base = int(raw_input('valor inicial <entero positivo>: '))
limite = int(raw_input('valor limite <entero positivo>: '))
incremento = int(raw_input('valor del incremento <entero positivo>: '))

#proccesing
if limite < 0 or incremento <= 0 or base < 0 or limite < base:
    print 'no es posible la operacion'
else:
    while base < limite:
        print base
        base *= incremento
print 'Hecho'