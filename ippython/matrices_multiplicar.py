# -*- coding: utf-8 -*-
"""
Created on Sun May  5 09:32:01 2013

@author: daniel
"""

#programa: matrices_multiplicar.py
#calcula el producto de dos matrices <A> y <B>
#solo y solo: A(pXq) y B(qXr) se cumple
#si el numero de columnas de <A> es igual al numero de filas de <B>

#paso 1: dimension de la primera matriz y columnas de la segunda
p = int(raw_input('Filas de <A>: '))
q = int(raw_input('Columnas de <A> y Filas de <B>: '))
r = int(raw_input('Columnas de <B>: '))

#paso 2: creamos dos matrices nulas

A = []
for i in range(p):
    A.append([0] * q)
    
B = []
for i in range(q):
    B.append([0] * r)
    

#paso 3: leemos su contenido del teclado

print 'Lectura de la Matriz <A>'
for i in range(p):
    for j in range(q):
        A[i][j] = float(raw_input('  Componente (%d, %d)' %(i,j)))
        
print 'Lectura de la Matriz <B>'
for i in range(q):
    for j in range(r):
        B[i][j] = float(raw_input('  Componente (%d, %d)' %(i,j)))
        
#paso 4: creamos una matriz nula <C> para albergar el resultado

C = []
for i in range(p):
    C.append([0] * r)
    
#paso 5: calculamos el producto de ambas matrices
for i in range(p):
    for j in range(r):
        for k in range(q):
            C[i][j] = A[i][k] * B[k][i]
            
#paso 6: mostramos el resultado en pantalla

print 'Producto: '
for i in range(p):
    for j in range(r):
        print C[i][j],
    print
print C
        