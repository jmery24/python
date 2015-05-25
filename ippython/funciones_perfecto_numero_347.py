# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 06:30:11 2013

@author: daniel
"""

#programa: funciones_perfecto_numero_347.py
#definir un procedimiento para seleccionar los numeros perfectos que 
#puedan estar en una lista dada
#ejercicio 347

#definir procedimiento <perfecto>
def perfecto(lista):
    nueva = []
    for j in lista:
        sumatorio = 0
        for i in range(1, j):
            if j % i == 0:
                sumatorio += i
        if sumatorio == j:                 
            nueva.append(sumatorio)
    return nueva
    
#cuerpo del programa
#input
numeros = [1, 6, 15, 28, 300, 496]

#activa procedimiento
print 'Numeros perfecto: ', perfecto(numeros)