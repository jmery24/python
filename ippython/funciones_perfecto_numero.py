# -*- coding: utf-8 -*-
"""
Created on Sun May 26 07:32:33 2013

@author: daniel
"""

#programa: funciones_numero_perfecto.py
#dado un <numero> calcula los numeros perfectos entre 1 y <numero>
#crear dos funciones

#crea: una funcion y un procedimiento
#definir funcion <es_perfecto>
def es_perfecto(num):
    sumatorio = 0
    for i in range(1, num):
        if num % i == 0:
            sumatorio += i
    return sumatorio == num

#definir procedimiento <tabla_perfectos>, funcion sin 'return', es un procedimiento
def tabla_perfectos(nro):
    for i in range(1, nro+1):
        if es_perfecto(i):
            print i, 'Es un numero perfecto'
            
#cuerpo del programa

#data input
numero = int(raw_input('Escribe un numero: '))

#activa funcion
tabla_perfectos(numero)   