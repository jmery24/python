# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 06:17:23 2013

@author: daniel
"""

#programa: funciones_sumadiagonal_356.py
#definir una funcion que sume la diagonal principal
#si m = n en la matriz mxn, si es diferente = none
#ejercicio 356

#definir la funcion <suma_diagonal>
def suma_diagonal(matriz, columnas, filas):
    suma = []
    if columnas != filas:
        print None
    else:
        for i in range(filas):
            for j in range(columnas):
                if i == j:
                    suma.append(matriz[i][j])
    return sum(suma)

#cuerpo del programa
#input
            #definimos tamanio de la matriz
print '   Matriz de (filas X columnas)'
n = int(raw_input('numero de filas: '))
m = int(raw_input('numero de columnas: '))
print
            #creamos una matriz nula
M = []
for i in range(n): #creamos una matriz nula
    M.append([0]*m)
            #leemos su contenido desde el teclado
print '   Componentes de la matriz'
for j in range(n):
    for k in range(m):
        M[j][k] = float(raw_input('Dame el componente (%d,%d): ' %(j,k)))
print
print '   Matriz de',len(M), 'X', len(M[0])
print M

#activa funcion
print
print 'Suma de la diagonal principal: ', suma_diagonal(M, m, n)