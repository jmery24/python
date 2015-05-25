# -*- coding: utf-8 -*-
"""
Created on Sun May  5 12:29:01 2013

@author: daniel
"""

#programa: matrices_traspuestas.py
#crear una matriz de (nXm) y su traspuesta

print '     Matriz de (filas X columnas)'
n = int(raw_input('numero de filas: '))
m = int(raw_input('numero de columnas: '))

#creamos una matriz nula
M = []
for i in range(n): #creamos una matriz nula
    M.append([0]*m)

#asignamos valores a la matriz desde el teclado
for j in range(n):
    for k in range(m):
        M[j][k] = float(raw_input('   Dame el componente (%d,%d): ' %(j,k)))
print
print '     Matriz de',len(M), 'X', len(M[0])
print M

#crea matriz nula <T>, T(m X n), ojo invierte la <n> y la <m>

T = []
for i in range(m):
    T.append([0]*n)
#print
#print '   Matriz nula <T> de',n, 'X', m
#print T
#print

#transforma matriz <M> en su Transpuesta y la alberga en <T>

for i in range(m):
    for j in range(n):
        T[i][j] = M[j][i]
print
print 'Matrix <T> transpuesta de matriz <M>'
print T