# -*- coding: utf-8 -*-
"""
Created on Fri May 10 18:22:26 2013

@author: daniel
"""

#programa: funciones_perfecto_275.py
#calcula los numeros perfectos entre 1 y n
#ejercicio 275

#definir funcion <perfecto>
def perfecto(num):
    lista = []
    for j in range(1,num):       
        sumatorio = 0
        for i in range(1, j):
            if j % i == 0:
                sumatorio += i
        if sumatorio == j:                 
            lista.append(sumatorio)
    return lista
        
#cuerpo principal del programa        
#data input
numero = int(raw_input('Introduzca un numero: '))

#activa funcion
print 'Lista de numeros perfectos entre 1 y', numero, ':', perfecto(numero)