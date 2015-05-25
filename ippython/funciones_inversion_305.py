# -*- coding: utf-8 -*-
"""
Created on Sun May 26 09:52:29 2013

@author: daniel
"""

#programa: funciones_inversion_305.py
#escribe un procedimiento para invertir un numero entero
#ejemplo: input = 324, output = 4 2 3 en lineas diferentes
#ejercicio 305

#definir el procedimiento <inversion>
def inversion(num):
    invertido = 0
    while num > 0:
        invertido = invertido * 10 + num % 10
        num = num / 10
    cadena = str(invertido)
    for i in range(0, len(cadena)):
        print cadena[i]

#cuerpo general del programa

#data input
numero = int(raw_input('Escribe un numero entero: '))

#activa el procedimiento
inversion(numero)