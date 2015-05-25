# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 07:20:35 2013

@author: daniel
"""

#programa: matriz.py
#modulo aplicable a matrices

#definir funciones

#definir <matriz_nula>
def matriz_nula(filas, columnas):
    M = []
    for i in range(filas):
        M.append([0]  * columnas)
    return M
#definir <lee_matriz>
def lee_matriz(filas, columnas):
    M = matriz_nula(filas, columnas)
    for i in range(filas):
        for j in range(columnas):
            M[i][j] = float(raw_input('Introduce el componente (%d,%d): ' %(i, j)))
    return M
#definir la funcion <dimension>
def dimension(M):
    return [len(M), len(M[0])]
#definir funcion <es_cuadrada>
def es_cuadrada(M):
    forma = dimension(M)
    if forma[0] == forma[1]:
        return True
    else:
        return False
#definir la funcion <suma>
def suma(A, B):
    if dimension(A) != dimension(B):
        return None
    else:
        [m, n] = dimension(A)
        C = matriz_nula(m, n)
        for i in range(m):
            for j in range(n):
                C[i][j] = A[i][j] + B[i][j]
    return C
#definir funcion <multiplica>
def multiplica(A, B):
    if dimension(A) != dimension(B):
        return None
    else:
        [m, n] = dimension(A)
        C = matriz_nula(m, n)
        for i in range(m):
            for j in range(n):
                C[i][j] = A[i][j] * B[i][j]
    return C
    
#prueba de las funciones del modulo, no funciona cuando se lo invoca
if __name__ == '__main__':
    filas = 2
    columnas = 2
    B = [[5.0, 6.0], [7.0, 8.0]]
    print 'Matriz nula: ', matriz_nula(filas, columnas)
    print
    A = lee_matriz(filas, columnas)
    print 'Matriz A: ', A
    print 'Matriz B: ', B
    print 'Dimension de la matriz: ', dimension(A)
    print 'La matriz A es cuadrada ?',es_cuadrada(A)
    print 'Suma A + B: ', suma(A, B)
    print 'Producto A x B: ', multiplica(A, B)     