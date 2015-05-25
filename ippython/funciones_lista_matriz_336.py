# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 06:53:07 2013

@author: daniel
"""

#programa:funciones_lista_matriz_336.py
#input: dos listas de numeros, lista A y lista B
#output: matriz C.... C = [[elemento_A0, elemento_B0].......]
#ejercicio 336

#definir la funcion <lista_matriz>
def lista_matriz(lista_a, lista_b):
    matriz_c = []
    for elemento_1 in lista_a:
        for elemento_2 in lista_b:
            matriz_c += [[elemento_1, elemento_2]]
    return matriz_c
    
#cuerpo del programa
#data input
A = [1, 3, 5]
B = [2, 5]

#activa la funcion
print 'la matriz es: ', lista_matriz(A, B) 