# -*- coding: utf-8 -*-
"""
Created on Sat May  4 06:36:11 2013

@author: daniel
"""

#programa: matrices_248.py
#crear una matriz identidad de axa
print '   Matriz Identidad de axa'
num_a = int(raw_input('valor <a> de la matriz: '))
m = []
for i in range(num_a):
    m.append([0]*num_a)
print '   Matriz nula de',num_a, 'X', num_a
print m

for j in range(num_a):
    m[j][j] = 1
print '   Matriz identidad de',num_a, 'X', num_a
print m