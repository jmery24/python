# -*- coding: utf-8 -*-
"""
Created on Sun May  5 07:26:02 2013

@author: daniel
"""

#programa: matrices_suma.py
#suma dos matrices (que deben tener la misma dimension)

#paso 1: Dimension de la matriz
m = int(raw_input('Numero de Filas: '))
n = int(raw_input('Numero de Columnas: '))

#paso 2: Creamos dos matrices nulas

A = []
for i in range(m):
    A.append([0] * n)
    
B = []
for i in range(m):
    B.append([0] * n)

#paso 3: leemos el contenido de cada matriz desde el teclado

print 'Lectura de la Matriz <A>'
for i in range(m):
    for j in range(n):
        A[i][j] = float(raw_input('Componentes de la Matriz (%d, %d):' %(i,j)))
    
print 'Lectura de la Matriz <B>'
for i in range(m):
    for j in range(n):
        B[i][j] = float(raw_input('Componentes de la Matriz (%d, %d):' %(i,j)))

#paso 4: construimos otra matriz nula para albergar el resultado

C = []
for i in range(m):
    C.append([0] * n)
    
#paso 5: calculo de la suma
for i in range(m):
    for j in range(n):
        C[i][j] = A[i][j] + B[i][j] 
        
#paso 6: mostramos el resultado en la pantalla

print
print 'Suma: '
for i in range(m):
    for j in range(n):
        print C[i][j]
    print

print 'Matriz C: ', C