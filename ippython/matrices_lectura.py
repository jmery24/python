# -*- coding: utf-8 -*-
"""
Created on Sat May  4 07:10:01 2013

@author: daniel
"""

#programa: matrices_lectura.py
#crear una matriz de nxm

print '   Matriz de (filas X columnas)'
n = int(raw_input('numero de filas: '))
m = int(raw_input('numero de columnas: '))

#creamos una matriz nula
M = []
for i in range(n): #creamos una matriz nula
    M.append([0]*m)
print '   Matriz nula de',n, 'X', m
print M

#leeemos su contenido desde el teclado
for j in range(n):
    for k in range(m):
        M[j][k] = float(raw_input('Dame el componente (%d,%d): ' %(j,k)))
print '   Matriz de',len(M), 'X', len(M[0])
print M

#formas de calcular la dimension de una matriz
print '  dos maneras de calcular la dimension de una matriz'
print 'dimension de la matriz: ', n, 'X', m
print 'dimension de la matriz: ', len(M), 'X', len(M[0])