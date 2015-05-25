# -*- coding: utf-8 -*-
"""
Created on Sun May  5 08:07:42 2013

@author: daniel
"""

#programa: matrices_251.py
#multiplica una matriz por un numero (miltiplica cada elemento de la matriz 
#por el numero)
#ejercicio 251

#paso 1: Dimension de la matriz y numero
m = int(raw_input('Numero de Filas: '))
n = int(raw_input('Numero de Columnas: '))
num = int(raw_input('Factor para multiplicar la matriz: '))

#paso 2: Creamos una matriz nula

A = []
for i in range(m):
    A.append([0] * n)
    
#paso 3: leemos el contenido de la matriz desde el teclado

print 'Lectura de la Matriz'
for i in range(m):
    for j in range(n):
        A[i][j] = float(raw_input('Componentes de la Matriz (%d, %d):' %(i,j)))
    
#paso 4: construimos otra matriz nula para albergar el resultado

C = []
for i in range(m):
    C.append([0] * n)
    
#paso 5: calculo de la multiplicacion matriz A por num
for i in range(m):
    print 'i', i
    for j in range(n):
        print 'j', j
        C[i][j] = A[i][j] * num
    
#paso 6: mostramos el resultado en la pantalla

print
print 'Resultado: '
for i in range(m):
    for j in range(n):
        print C[i][j]
    print

print 'Matriz C: ', C