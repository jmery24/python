# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 08:11:43 2013

@author: daniel
"""

#programa: funciones_compara_370.py
#definir funcion para comparar dos numeros naturales
#ejercicio 370

#definir funcion <compara>
def compara(a, b):
    if b == 0:
        return False
    elif a == 0:
        return True
    else:
        return compara(a - 1, b - 1)
        
#cuerpo del programa

#input
num_a = int(raw_input('Escribe un numero natural: '))
num_b = int(raw_input('Escribe otro numero natural: '))

#activa funcion
print
print 'Comparacion de ', num_a, 'y', num_b, ':', compara(num_a, num_b) 