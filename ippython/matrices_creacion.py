# -*- coding: utf-8 -*-
"""
Created on Sat May  4 06:07:44 2013

@author: daniel
"""

#programa: matrices_creacion.py
#crear una matriz nula de 6x3

a = [0] * 6
m = [a] * 3
print 'Matriz nula de 6x3'
print m
print 'modificamos m[0][0]'
m[0][0] = 1
print m
print 'modifica tambien m[1][0] y m[2][0]'

#creacion de una matriz de una matriz nula 4x3
m1 = [[0]*4]*3
print 'Matriz nula de 4x3'
print m1
print 'modificamos m1[0][0]'
m1[0][0] = 1
print m1
print 'modifica tambien m1[1][0] y m1[2][0]'

#metodo correcto de crear una matriz
m2 = []
for i in range(3):
    m2.append([0]*6)
print ' Matriz nula de 6x3'
print m2
print 'modificamos m1[0][0]'
m2[0][0] = 1
print m2
print 'no modifica m1[1][0] y m1[2][0]'