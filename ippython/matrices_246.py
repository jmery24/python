# -*- coding: utf-8 -*-
"""
Created on Sat May  4 04:42:09 2013

@author: daniel
"""

#programa: matrices_246.py
#ejercicio 246

m = [[1,0,0],[0,1,0],[0,0,1]]
print m[-1][0]
print m[-1][-1]
print '--'
for i in range(0,3):
    for j in range(0,3):
        print m[i][j],

#ejercicio 247

m1 = [[1,0,0],[0,1,0],[0,0,1]]
s = 0.0
for i in range(0,3):
    for j in range(0,3):
        s += m1[i][j]
print 'valor de (s): ',s
print '(s/9.0)=', s / 9.0