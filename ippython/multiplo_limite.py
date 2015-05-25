# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 07:18:42 2013

@author: daniel
"""

#programa:multiplo.py
#calcula los multiplos de numero en el intervalo [numero, limite]
#data input
num = 1
repeticiones = int(raw_input('valor limite <entero positivo>: '))
multiplo = int(raw_input('multiplos del numero: '))


#proccesing
if repeticiones < 0:
    print 'no es posible la operacion'
else:
    while num <= repeticiones / multiplo: #calcula los multiplos por numero limite
        print multiplo * num 
        num += 1
        
print 'Hecho'